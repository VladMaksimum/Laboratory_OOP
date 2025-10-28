import re
from ILogFilter import ILogFilter
from labs.lab_3.LogLevel import LogLevel

class ReLogFilter(ILogFilter):
    def __init__(self, pattern: str) -> None:
        self.pattern = pattern

    def match(self, log_level: LogLevel, text: str) -> bool:
        if re.fullmatch(self.pattern, text) == None:
            return False
        
        return True