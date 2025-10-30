from labs.lab_3.LogLevel import LogLevel

class ILogHandler:
    def handle(self, log_level: LogLevel, text: str) -> None:
        ...