from labs.lab_3.LogLevel import LogLevel
from ILogHandler import ILogHandler

class ConsoleHandler(ILogHandler):

    def handle(self, log_level: LogLevel, text: str) -> None:
        print(text)