"""
Configuration file.
This file loads setup configuration from the <setup.json> file.
"""

import json
from .const import (
    FP_BOOT_SETUP_FILE_NAME,
    FWM_READ
)


def load_setup():
    """
    This function returns setup-file data in dict format.
    <JSON_DATA> => <PYTHON_DICT>
    """
    return json.load(
        open(FP_BOOT_SETUP_FILE_NAME, FWM_READ)
    )


# Application setup
APPLICATION_SETUP = load_setup()


