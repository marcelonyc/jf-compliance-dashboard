import requests
from config.app_config import get_settings
import json

app_config = get_settings()
auth_heather = {"Authorization": f"Bearer {app_config.JF_TOKEN}"}


def call_get(endpoint: str, data: dict = None) -> dict:
    JF_URL = app_config.JF_URL
    url = f"{JF_URL}/{endpoint}"
    headers = auth_heather
    if data is None:
        response = requests.get(url, headers=headers)
    else:
        response = requests.get(url, headers=headers, data=json.dumps(data))

    return response.json()


def call_post(endpoint: str, data: dict = {}) -> dict:
    JF_URL = app_config.JF_URL
    url = f"{JF_URL}/{endpoint}"
    headers = auth_heather
    headers["Content-Type"] = "application/json"
    if data is {}:
        response = requests.post(url, headers=headers)
    else:
        response = requests.post(url, headers=headers, data=json.dumps(data))

    return response.json()


def call_aql(query: str) -> dict:
    JF_URL = app_config.JF_URL
    url = f"{JF_URL}/artifactory/api/search/aql"
    headers = auth_heather
    headers["Content-Type"] = "text/plain"
    response = requests.post(url, headers=headers, data=query)

    return response.json()
