from service.lib.api import call_post, call_get


def get_violations(data: dict):
    return call_post("xray/api/v1/violations", data)


def get_watches():
    return call_get("xray/api/v2/watches")


def get_policies():
    return call_get("xray/api/v2/policies")
