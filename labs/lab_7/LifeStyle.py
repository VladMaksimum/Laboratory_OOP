from typing import Any
from abc import abstractmethod

class LifeStyle:
    def __init__(self, class_type: type, params: list[str]) -> None:
        self._class_type = class_type
        self._params = params
    
    @abstractmethod
    def create_instance(self, params: dict[str, Any] | None = None) -> Any:
        ...
    