"""
Configuration file.
This file contains application constants and other static variables.

VARIABLE TAG RULES:
    FP (FILE PATH) - variable with this tag contains filename or filepath;
    TK (TOKEN) - variable with this tag contains private key or token;
    FWM (FILE WORK MODE) - variable with this tag contains file work mode: (r, w, rb, wb);
    SP (STRING PATTERN) - variable with this tag contains string pattern: ({}x{}.format(a, b));
    JSHD (JSON SETUP HEADER) - variable with this tag contains <SETUP_DICT_KEY>;
    LK (LOGGING CONFIGURATION) - variable with this tag contains <logging.baseConfig()> values.
    WM - others.
"""

import win32api

# Tokens and others
TK_TELEGRAM_BOT_TOKEN: str
TK_API_SERVICE_URL: str
TK_API_SERVICE_PRIVATE_KEY: str
TK_ADMINISTRATOR_ID: int
TK_ADMINISTRATOR_NAME: str
TK_USERS: list
APP_NONE_STOP: bool


# Work Space (ENV)
FP_ENV_FOLDER = win32api.GetTempPath()
FP_USERS_DATA_FILE_NAME = "hxx-user-data.json"
FP_ENCRYPTION_KEY_FILE_NAME = "hxx-dtc-private.key"
FP_BOOT_SETUP_FILE_NAME = "setup.json"
FP_LOG_FILE_NAME = "hxx-log.log"

# File work modes
FWM_READ = "r"
FWM_READ_BYTES = "rb"
FWM_WRITE = "w"
FWM_WRITE_BYTES = "wb"

# String patterns
SP_JOIN_PATH = "{}/{}"
SP_LOG_EVENT = "ID: {}; NAME: {}; COMMAND: {};"
SP_LOG_ERROR = "ID: {}; NAME: {}; COMMAND: {}; ERROR: {}"


# Json setup headers
JSHD_USE_PROXY = "use_proxy"
JSHD_USE_PERMISSIONS_SYSTEM = "permission_system"
JSHD_ADMINISTRATOR_ID = "administrator_id"
JSHD_ADMINISTRATOR_NAME = "administrator_name"
JSHD_ACCESS_TOKEN = "access_token"
JSHD_API_SERVICE_URL = "api_service"
JSHD_API_SERVICE_KEY = "api_private"
JSHD_SERVER_NONE_STOP = "none_stop"
JSHD_ADD_TO_STARTUP = "add_to_startup"
JSHD_USERS = "users"

# Logging configuration
LK_SETUP = {
    "level": "INFO",
    "filename": SP_JOIN_PATH.format(FP_ENV_FOLDER, FP_LOG_FILE_NAME),
    "format": "[%(asctime)s] - [%(levelname)s] -> %(message)s"
}

# Others
WM_STARTUP_KEY_VALUE = r"Software\Microsoft\Windows\CurrentVersion\Run"
