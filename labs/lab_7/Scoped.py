from LifeStyle import LifeStyle
from typing import Any
from Scope import Scope


class Scoped(LifeStyle):
    def __init__(self, class_type: type, params: list[str], scope: Scope) -> None:
        super().__init__(class_type, params)
        self._instance = None
        self._scope = scope

    def create_instance(self, interface_type: type, params: dict[str, Any] | None = None) -> Any:
        if self._instance == None:
            if self._params == []:
                return self._class_type()

            elif params != None:
                return self._class_type(**params)
        
        return self._instance
    