#! /bin/bash

# This script import the pre-defined dashboards into Superset.
# The import requires docker/.env-local-jfrog or .env-local file to be present
# .env-local-jfrog content trakes precedence over .env-local

log_file = "/tmp/import-dashboards_${RANDOM}.log"
exec > >(tee -a ${log_file} )
exec 2> >(tee -a ${log_file} >&2)
exec 2>&1

echo "Log file: ${log_file}"

log_error () {
    echo -e "[`date`]\033[31mERROR: $1\033[0m"
}

log_info () {
    echo -e "[`date`]\033[32mINFO: $1\033[0m"
}

EXPORTS_DIR="/tmp/exports"
log_info "Creating exports directory in the container"
docker exec superset_app bash -c "mkdir -p ${EXPORTS_DIR}"
if [ $? -ne 0 ]; then
    log_error "Failed to create exports directory in the container"
    exit 1
else
    log_info "Exports directory created successfully"
fi

log_info "Copying exports to the container"
docker cp docker/exports/ superset_app:/tmp/
if [ $? -ne 0 ]; then
    log_error "Failed to copy exports to the container"
    exit 1
else
    log_info "Exports copied successfully"
fi

log_info "Copying publish.py to the container"
docker cp docker/dashboard-publish/publish.py superset_app:${EXPORTS_DIR}
if [ $? -ne 0 ]; then
    log_error "Failed to copy publish.py to the container"
    exit 1
else
    log_info "publish.py copied successfully"
fi

log_info "Copying import-dashboards.sh to the container"
docker cp docker/dashboard-publish/import-dashboards.sh superset_app:${EXPORTS_DIR}
if [ $? -ne 0 ]; then
    log_error "Failed to copy import-dashboards.sh to the container"
    exit 1
else
    log_info "import-dashboards.sh copied successfully"
fi

env_local_jfrog=""
if [ -f docker/.env-local ]; then
    env_local_jfrog=" --env-file docker/.env-local "
fi
env_local=""
if [ -f docker/.env-local-jfrog ]; then
    env_local="--env-file docker/.env-local-jfrog"
fi

if [ "${env_local}x" == 'x' ] && [ "${env_local_jfrog}x" == 'x' ]
then
    echo "No .env-local or .env-local-jfrog file found. Exiting..."
    exit 1
fi

log_info "Update dashboard metadata"
docker exec -e EXPORTS_DIR=${EXPORTS_DIR} ${env_local} ${env_local_jfrog} superset_app bash -c "cd ${EXPORTS_DIR} && python publish.py"
if [ $? -ne 0 ]; then
    log_error "Failed to update dashboard metadata"
    exit 1
else
    log_info "Dashboards metadata updated successfully"
fi

log_info "Publishing dashboards"
docker exec -e EXPORTS_DIR=${EXPORTS_DIR} ${env_local} ${env_local_jfrog} superset_app bash -c "cd ${EXPORTS_DIR} && ./import-dashboards.sh"
if [ $? -ne 0 ]; then
    log_error "Failed to publish dashboards"
    exit 1
else
    log_info "Dashboards published successfully"
fi
