from enum import Enum

class Colors(Enum):
    RED = '\x1b[31m'
    GREEN = '\x1b[32m'
    BLUE = '\x1b[34m'
    BLACK = '\x1b[30m'
    WHITE = '\x1b[37m'
    DEFAULT = '\x1b[39m'
