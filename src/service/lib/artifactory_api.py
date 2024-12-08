from service.lib.api import call_post, call_get, call_aql


def get_all_repos():
    return call_get("artifactory/api/repositories/configurations")


def get_updated_repo_list(query):
    return call_aql(query)


def get_license_info(repos):
    return call_get(f"artifactory/api/search/license?repos={repos}")
