import sys
import os
import logging

match sys.platform:
    case 'win32':
        USER_NAME_VAR = "USERNAME"
    case 'darwin'|'linux': 
        USER_NAME_VAR = 'USER'
    case _:  # default
        raise Exception("Unknown OS")

USER_NAME = os.getenv(USER_NAME_VAR)

logging.basicConfig(
    format=f'%(levelname)s %(name)s %(asctime)s {USER_NAME} %(filename)s %(lineno)d %(message)s', # set the format for log entries
    datefmt="%x-%X",
    filename='../LOGS/formatted.log',
    level=logging.DEBUG,
)
# logger = logging.getLogger('LuthorCorp')

logging.debug("User name is %s", USER_NAME)
logging.info("this is information")
logging.warning("this is a warning")
logging.debug("Wombats are fun")
logging.error("this is an ERROR")
value = 38.7
logging.error("Invalid value %f", value)
logging.info("this is information")
logging.critical("this is critical")

