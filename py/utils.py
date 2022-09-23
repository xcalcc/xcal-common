import json
import logging
import os
import re

from xcal_common.py.error import XcalError

_ERROR_MESSAGE_FILE_NAME = "errorMessage.json"
_ERROR_MESSAGE_FILE = os.path.join(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))), _ERROR_MESSAGE_FILE_NAME)

# basic check for error message file
if not os.path.isfile(_ERROR_MESSAGE_FILE):
    raise FileNotFoundError("File not found: %s" % _ERROR_MESSAGE_FILE)
if not os.access(_ERROR_MESSAGE_FILE, os.R_OK):
    raise PermissionError("Cannot read file: %s" % _ERROR_MESSAGE_FILE)
if os.path.getsize(_ERROR_MESSAGE_FILE) == 0:
    raise ValueError("File is empty: %s" % _ERROR_MESSAGE_FILE)


def get_canonical_error_name(xcal_error: XcalError):
    logging.debug("xcal_error: %s" % xcal_error)
    if not isinstance(xcal_error, XcalError):
        logging.error("xcal_error should be an instance of XcalError!")
        assert False, "internal errors occur!"
    camel_name = xcal_error.__class__.__name__
    canonical_error_name = (camel_name[0].upper()+re.sub(r'[A-Z]', lambda x: '_' + x.group(0), camel_name[1:])).upper()
    logging.debug("canonical error name: %s" % canonical_error_name)
    return canonical_error_name


def get_error_message(xcal_error: XcalError, language="en"):
    logging.debug("xcal_error: %s" % xcal_error)
    canonical_error_name = get_canonical_error_name(xcal_error)

    try:
        with open(_ERROR_MESSAGE_FILE) as json_file:
            error_message = json.load(json_file)
            error_keys = dict(error_message.get("errors"))
            logging.debug("all error keys: %s" % error_keys)

        return error_keys.get(canonical_error_name).get("err_message").get(language)
    except Exception as err:
        logging.error(err)
        assert False, "internal errors occur!"


