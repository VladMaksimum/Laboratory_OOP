from abc import ABC


class MailService(ABC):
    ...

class Database(ABC):
    ...

class Logger(ABC):
    ...


class GmailService(MailService):
    ...

class YmailService(MailService):
    ...


class SQLDB(Database):
    def __init__(self, connection_str: str):
        self.connection_str = connection_str

class MongoDB(Database):
    ...


class ConsoleLogger(Logger):
    ...

class FileLogger(Logger):
    ...


class I1:
    ...

class I2:
    ...

class C1(I1):
    ...

class C2(I2):
    def __init__(self, i1: I1):
        self.i1 = i1