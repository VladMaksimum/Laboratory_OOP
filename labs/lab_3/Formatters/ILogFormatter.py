from lab_3.LogLevel import LogLevel

class ILogFormatter:
    def format(self, log_level: LogLevel, text: str) -> None:
        ...