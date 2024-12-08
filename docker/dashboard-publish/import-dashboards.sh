#! /bin/bash

EXPORTS_DIR=${EXPORTS_DIR:-"/tmp/exports"}
for file in `ls ${EXPORTS_DIR}/*.zip`
do
    superset import-dashboards -u admin -p $file
done