from typing import Any

class LifeStyle:
    def __init__(self, class_type: type, params: list[str]) -> None:
        self._class_type = class_type
        self._params = params
    
    def create_instance(self, interface_type: type, params: dict[str, Any] | None = None) -> Any:
        ...
    