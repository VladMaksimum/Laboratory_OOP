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
    ...

class MongoDB(Database):
    ...


class ConsoleLogger(Logger):
    ...

class FileLogger(Logger):
    ...
