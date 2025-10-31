from LogLevel import LogLevel
from Handlers.ILogHandler import ILogHandler

class FileHandler(ILogHandler):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def handle(self, log_level: LogLevel, text: str) -> None:
        with open(self.file_path, "a") as file:
            file.write(text + '\n')