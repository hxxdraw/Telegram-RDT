"""
Application. Telegram-Bot-Server
"""

import telebot
import logging
from settings import *
from cmodules import *


# Unloading setup
TK_TELEGRAM_BOT_TOKEN = APPLICATION_SETUP[JSHD_ACCESS_TOKEN]
TK_API_SERVICE_URL = APPLICATION_SETUP[JSHD_API_SERVICE_URL]
TK_API_SERVICE_PRIVATE_KEY = APPLICATION_SETUP[JSHD_API_SERVICE_KEY]
TK_ADMINISTRATOR_ID = APPLICATION_SETUP[JSHD_ADMINISTRATOR_ID]
TK_ADMINISTRATOR_NAME = APPLICATION_SETUP[JSHD_ADMINISTRATOR_NAME]
TK_USERS = APPLICATION_SETUP[JSHD_USERS]
APP_NONE_STOP = APPLICATION_SETUP[JSHD_SERVER_NONE_STOP]

# Creating <telebot.Telebot> object (SESSION)
session = telebot.TeleBot(APPLICATION_SETUP[JSHD_ACCESS_TOKEN])

# Configuring logging
logging.basicConfig(**LK_SETUP)

# DEV TOOL
# Outputting workspace and work files paths
[
    print(key, " -> ", on_start()[key]) for key in on_start().keys()
]


"""
Command response.
In this part server receives on all commands/messages sent by valid user.
If command header is valid -> server tries to response.
"""


def create_error_log(message: telebot.types.Message, command_header: str, error: str or object):
    """
    This function returns tuple with all requirements for logging (.format)
    :param message: telebot.types.Message
    :param command_header: str
    :param error: str or object
    :return: tuple
    """
    return SP_LOG_ERROR.format(
        message.from_user.id,
        message.from_user.username,
        command_header,
        error
    )


def create_event_log(message: telebot.types.Message, command_header: str):
    """
    This function returns tuple with all requirements for logging (.format)
    :param message: telebot.types.Message
    :param command_header: str
    :return: tuple
    """

    return SP_LOG_EVENT.format(
        message.from_user.id,
        message.from_user.username,
        command_header
    )


@session.message_handler(commands=HDDL_MAIN[HD_TEST_DEV])
def dev_test_response(message):
    """
    message type => object
    message.from_user.id type => int. (telegram id of message/command sender).
    message.from_user.username type => str/None. (telegram username of message/command sender).

    Operations sequence:
        1. Receiving message.
        2. Checking sender-id validity:
          2.1. If id is valid => trying to response.
          2.2. If id isn't valid => ignore.
          2.3. If id is valid but something was wrong => saving log.
    """
    try:
        if message.from_user.id == TK_ADMINISTRATOR_ID:
            # sending an object <message> to telegram
            session.send_message(message.from_user.id, message)

            # outputting an object <message> to the console
            print(message)

            # creating event log
            logging.info(
                create_event_log(
                    message,
                    HD_TEST_DEV
                )
            )

    except Exception as e:
        # Server saves information about errors if something was wrong
        logging.error(
            create_error_log(
                message,
                HD_TEST_DEV,
                e
            )
        )


# Server polling
session.polling(none_stop=APP_NONE_STOP)
