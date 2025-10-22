#Логгер

from abc import ABC, abstractmethod

class DumbLogger:
    def __init__(self, logger_type: str, file_path: str= None, host: str= None,\
                port: str= None, url: str= None, login: str= None, password: str = None) -> None:
        self.logger_type = logger_type
        self.file_path = file_path
        self.host = host
        self.port = port
        self.url = url
        self.login = login
        self.password = password
    
    def log(text: str) -> None:
        if self.logger_type == "console":
            print(text)
        if self.logger_type == "file":
            try:
                with open(self.ile_path, "w") as file:
                    file.write(text)
            except:
                pass
        if self.logger_type == "socket":
            pass
        
        if self.logger == "ftp":
            pass

class Logger(ABC):
    @abstractmethod
    def log(self, text: str) -> None:
        ...


class ConsoleLogger(Logger):
    def log(self, text: str) -> None:
        print(text)

class FileLogger(Logger):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
    def log(self, text: str) -> None:
        try:
            with open(self.ile_path, "w") as file:
                file.write(text)
        except:
            pass

class SocketLogger(Logger):
    def __init__(self, host: str, port: str) -> None:
        self.host = host
        self.port = port
    
    def log(self, text: str) -> None:
        pass

class FiltredLogger(Logger):
    @abstractmethod
    def filter(self, text) -> bool:
        ...
    @abstractmethod
    def _log(self, text: str) -> None:
        ...
        
    def log(self, text: str) -> None:
        if not self.filter(text):
            return
        self._log(text)

class SubstringFilteredLogger(FiltredLogger):
    def __init__(self, filter_str: str) -> None:
        self.filter_str = filter_str
    def filter(self, text) -> bool:
        return self.filter_str.lowe() in text.lower()

import re

class RegExFilteredLogger(FilteredLogger):
    def __init__(self, pattern: str) -> None:
        self.pattern = pattern
    
    def filter(self, text) -> bool:
        pass
        #return re.match(self.pattern, text) in not None
class ConsoleSimpleFilteredLogger(ConsoleLogger, SubstringFilteredLogger):
    def __init__(self, filter_str: str) -> None:
        SubstringFilteredLogger.__init__(self, filter_str)
    def _log(self, text: str) -> None:
        ConsoleLogger.log(self, text)


class A:
    ...
class B(A): #наследывание
    ...

class B1:
    def __init__(self, a: A):
        self.a = a #agregasion

class B2:
    def __init__(self):
        self.a = A() #composition

class Handler(ABC):
    @abstractmethod
    def handle(self, text: str) -> None:
        ...

class ConsoleHandler(Handler):
    def handle(self, text: str) -> None:
        print(text)

class FileHandler(Handler):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
    def handle(self, text: str) -> None:
        try:
            with open(self.file_path, "w") as file:
                file.write(text)
        except:
            pass

class SocketHandler(Handler):
    def __init__(self, host: str, port: str) -> None:
        self.host = host
        self.port = port
    
    def handle(self, text: str) -> None:
        pass

class Filter(ABC):
    @abstractmethod
    def filter(self, text: str) -> None:
        ...

class SimpleFilter(Filter):
    def __init__(self, filter_str: str) -> None:
        self.filter_str = filter_str
    def filter(self, text) -> bool:
        return self.filter_str.lowe() in text.lower()
    
class RegExFilter(Filter):
    def __init__(self, pattern: str) -> None:
        self.pattern = pattern
    
    def filter(self, text) -> bool:
        pass
        #return re.match(self.pattern, text) in not None

class SmartLogger(Logger):
    def __init(self, handlers: List[Handler], filters: list[Filter]) -> None:
        self.handlers = handlers
        self.filters = filters

    def log(self, text: str) -> None:
        if not all(filt.filter(text) for filt in self.filters):
            return
        
        for handler in handlers:
            handler.handle(text)

logger = SmartLogger(handlers = [ConsoleHandler(), FileHandler("log.txt")], \
                    filters = [SimpleFilter("ERROR"), RegExFilter("*")])
logger.log("ERROR something happened")
logger.log("Debug")
