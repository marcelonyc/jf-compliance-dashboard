from service.lib.api import call_post, call_get


def get_all_repos():
    return call_get("artifactory/api/repositories/configurations")
