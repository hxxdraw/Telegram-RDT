"""Module file"""

import requests
from settings import *
from urllib.request import urlretrieve

# Const
DOT_SEPARATOR = "."
SLASH_SEPARATOR = "/"


def create_api_request():
    """
    This function creates API-request to the selected service form the <setup.json> file.
    Also, this function returns dict with all net-information about user. (ip, domain, latitude, longitude and other).
    :return: dict
    """

    return requests.get(TK_API_SERVICE_URL + TK_API_SERVICE_PRIVATE_KEY).json()


def download_file(url: str):
    """
    This function downloads file and saves it to the WORKSPACE folder
    :return: str => <FULL_FILE_PATH>
    """

    # Splitting url to get file name
    url_slash_sp = url.split(SLASH_SEPARATOR)
    file_name = url_slash_sp[len(url_slash_sp) - 1]
    file_path = SP_JOIN_PATH.format(FP_ENV_FOLDER, file_name)
    urlretrieve(url, file_path)

    return file_path
