from lab_3.LogLevel import LogLevel
from ILogFormatter import ILogFormatter
import time

class SimpleFormatter(ILogFormatter):
    def format(self, log_level: LogLevel, text: str) -> None:
        return f'[{log_level.name} [{time.gmtime()}] {text}'
