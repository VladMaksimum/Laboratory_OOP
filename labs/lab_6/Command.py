from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def do_command(self) -> None:
        ...
    
    @abstractmethod
    def undo(self) -> None:
        ...
    
    @abstractmethod
    def redo(self) -> None:
        ...