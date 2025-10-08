#Наследывание

from abc import ABC, abstractmethod
from enum import Enum

class logger1():
    def __init__(self, logger_type:str, file_path:str, url:str, port:int) -> None:
        self.logger_type = logger_type
    
    def log(self, text:str) -> None:
        if self.logger_type == "console":
            print(text)
        elif self.logger_type == "file":
            with open("", "w+") as file:
                file.write(text)
        elif self.logger_type == "socket":
            ...
        elif self.logger_type == "email":
            ...
        elif self.logger_type == "ftp":
            ...


class logger2(ABC):
    @abstractmethod
    def log(self, text:str) -> None:
        ...

class ConsoleLogger(logger2):
    def log(self, text:str) -> None:
        print(text)
        
class FileLogger(logger2):
    def __init__(self, file_path:str) -> None:
        self.file_path = file_path
    
    def log(self, text:str) ->None:
        with open(self.file_path, "w+") as f:
            f.write(text)


class SimpleFilteredLogger(logger2, ABC):
    def __init__(self, filter_str:str) -> None:
        self.filter_str = filter_str
    
    def log(self, text:str) -> None:
        if filter_str in text:
            return
    
        self._log(text)
    @abstractmethod
    def _log(self, text:str) -> None:
        ...


class RegExFilteredLogger(logger2, ABC):
    def __init__(self, patern:str) -> None:
        self.patern = patern
    
    def log(self, text:str) -> None:
        if patern in text:
            return
    @abstractmethod
    def _log(self, text:str) -> None:
        ...


#Композиция и агрегация

class A:
    ...
    
class B:
    def __init__(self, a:A) -> None:
        self.a = a #aggregation

class C:
    def __init__(self):
        self.a = A() #composition (A exists while exists B)
    
class  Filter(ABC):
    @abstractmethod
    def do_filter(self, text) -> bool:
        ...

class SimpleFilter(Filter):
    def __init__(self, filter_str:str) ->None:
        self.filter_str = filter_str
        
    def do_filter(self, text) -> bool:
        return filter_str in text

class RegExFiter(Filter):
    def __init__(self, pattern:str) -> None:
        self.pattern = pattern
    
    def do_filter(self, text:str) -> bool:
        return re.match(self.pattern, text)

class Handler(ABC):
    @abstractmethod
    def handle(self, text:str):
        ...

class ConsoleHandler(Handler):
    def handle(self, text:str)-> None:
        print(text)

class FileHandler(Handler):
    def __init__(self, path:str) -> None:
        self.path = path
    
    def handle(self, text:str)-> None:
        with open(path, "w+") as f:
            f.write(text)

class EmailHandler(Handler):
    def __init__(self, server:str, email_from:str, email_to:str, title:str) ->None:
        ...
    
    def log(self, text:str) ->None:
        body = self._create_body(text)
        title = self._create_title(text)
    
    def _create_body(self,text):
        ...
    
    def _create_title(self,text):
        ...


class Levels(Enum):
    ERROR,
    WARNING,
    INFO

class LevelFilter(Filter):
    ...

class Logger:
    def __init__(self, filter_list:list[Filter], handlers:list[Handler]) -> None:
        self.filters = filters_list
        self.handlers = handlers
    
    def log(self, text:str) -> None:
        if not all(item_filter.do_filter(text) for item_filter in self.filters):
            return
        
        for handler in self.handlers:
            handler.handle(text)

logger = Logger(filters=[SimpleFilter("ERROR"), RegExFiter("(w+*)")], handlers = [ConsoleHandler(), FileHandler() ])

logger.log("an cabhbs")
