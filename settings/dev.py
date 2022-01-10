"""
This script uses only for application development
"""
from .const import *

# Dev const
KEY_WORKSPACE = "WORKSPACE"
KEY_LOG_FILE_NAME = "LOG_FILE"
KEY_SETUP_FILE_NAME = "SETUP_FILE"
KEY_LOG_FILE_FULL_PATH = "LOG_FILE_FP"


def on_start():
    """
    This function returns application boot configuration
    """
    return {
        KEY_WORKSPACE: FP_ENV_FOLDER,
        KEY_LOG_FILE_NAME: FP_LOG_FILE_NAME,
        KEY_SETUP_FILE_NAME: FP_BOOT_SETUP_FILE_NAME,
        KEY_LOG_FILE_FULL_PATH: SP_JOIN_PATH.format(FP_ENV_FOLDER, FP_LOG_FILE_NAME),
    }