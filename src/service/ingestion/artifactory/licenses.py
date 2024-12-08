from service.models.artifactory.models import (
    repo_updated_hwm_table,
    AQLRepoNames,
    LicenseResult,
    License,
)
from service.lib.artifactory_api import get_updated_repo_list, get_license_info
from database.database import database
from sqlalchemy import select, delete, insert, update
import datetime
from sqlalchemy.exc import IntegrityError


def update_license_inventory():

    # Get last updated timestamp
    query = select(repo_updated_hwm_table.updated_hwm)
    result = database.execute_sync(query)
    hwm = result.fetchone()
    hwms: datetime.datetime = (
        hwm[0] if hwm else datetime.datetime(1999, 1, 16, 0, 0)
    )
    hwms = hwms.replace(tzinfo=datetime.timezone.utc).strftime("%Y-%m-%d")
    # To set watermark to current date
    time_now = datetime.datetime.now().strftime("%Y-%m-%d")

    aql_query = (
        'items.find({"updated" : {"$gt":"'
        + hwms
        + '"}}).include("repo").distinct(true)'
    )

    repos = get_updated_repo_list(aql_query)

    all_repos = AQLRepoNames(**repos)

    # Distint does not seem to be working
    # in Jfrog results, so we will use a dict
    # to keep track of distinct repos
    repo_distinct = {}
    for _repo in all_repos.results:
        if repo_distinct.get(_repo.repo):
            continue
        else:
            repo_distinct[_repo.repo] = True

        try:
            license_results = License(**get_license_info(_repo.repo))
        except Exception as e:
            repos = ""
            continue

        for _result in license_results.results:
            _result.repo = _repo.repo
            try:
                database.execute_sync(
                    insert(LicenseResult).values(_result.model_dump())
                )
            except IntegrityError as e:
                database.execute_sync(
                    update(LicenseResult)
                    .where(LicenseResult.uri == _result.uri)
                    .values(
                        license=_result.license,
                        found=_result.found,
                        status=_result.status,
                        repo=_result.repo,
                    )
                )

    database.execute_sync(delete(repo_updated_hwm_table))

    database.execute_sync(
        insert(repo_updated_hwm_table).values(updated_hwm=time_now)
    )
