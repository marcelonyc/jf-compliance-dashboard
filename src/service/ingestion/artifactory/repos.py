from service.models.artifactory.models import ArtifactRepos as ArtifactoryModel
from service.lib.artifactory_api import get_all_repos
from database.database import database
from database.models.artifactory.models import (
    local_item_table,
    remote_item_table,
    virtual_item_table,
    federated_item_table,
    release_bundle_item_table,
)
from sqlalchemy import select, func, insert, update, and_ as _and


def get_all_artifactory_repos():

    # Clear tables
    database.execute_sync(local_item_table.delete())
    database.execute_sync(remote_item_table.delete())
    database.execute_sync(virtual_item_table.delete())
    database.execute_sync(federated_item_table.delete())
    database.execute_sync(release_bundle_item_table.delete())

    repos = get_all_repos()
    all_repos = ArtifactoryModel(**repos)
    for _repo in all_repos.LOCAL:
        database.execute_sync(
            insert(local_item_table).values(_repo.model_dump())
        )

    for _repo in all_repos.REMOTE:
        database.execute_sync(
            insert(remote_item_table).values(_repo.model_dump())
        )

    for _repo in all_repos.VIRTUAL:
        database.execute_sync(
            insert(virtual_item_table).values(_repo.model_dump())
        )

    for _repo in all_repos.FEDERATED:
        database.execute_sync(
            insert(federated_item_table).values(_repo.model_dump())
        )

    for _repo in all_repos.RELEASE_BUNDLE:
        database.execute_sync(
            insert(release_bundle_item_table).values(_repo.model_dump())
        )
