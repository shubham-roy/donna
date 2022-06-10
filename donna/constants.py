from enum import Enum
from os import getcwd
from os.path import expanduser, join


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


CURR_DIR = getcwd()
DONNA = "donna"
TIME_CONVERSION_FACTOR = 60
USER_HOME_DIR = expanduser("~")
DONNA_DIR = join(USER_HOME_DIR, f".{DONNA}")
LOG_FORMAT = (
    "{time} | {level: <8} | {name: ^50} | {function: ^20} | {line: >3} | {message}\n"
)
