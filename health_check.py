from consts import WEBSITE_URL, CONNECTION_SUCCESS, CONNECTION_FAILED, RESPONSE_DEFAULT_MESSAGE
from requests import HTTPError, ConnectionError
import requests

website = {
    "previous_status": "",
    "status": RESPONSE_DEFAULT_MESSAGE
}


def _check_consistent_health(status):
    if website["previous_status"] == status:
        return True
    return False


def check_website_health():
    try:
        response = requests.get(WEBSITE_URL)
        response.raise_for_status()
        if _check_consistent_health(CONNECTION_SUCCESS):
            website["status"] = CONNECTION_SUCCESS
        website["previous_status"] = CONNECTION_SUCCESS

    except (HTTPError, ConnectionError, Exception):
        if _check_consistent_health(CONNECTION_FAILED):
            website["status"] = CONNECTION_FAILED
        website["previous_status"] = CONNECTION_FAILED
