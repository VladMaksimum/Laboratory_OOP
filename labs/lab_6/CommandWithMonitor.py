from Command import Command
from Monitor import Monitor

class CommandWithMonitor(Command):
    def __init__(self) -> None:
        self._monitor = Monitor("labs/lab_6/test.txt")