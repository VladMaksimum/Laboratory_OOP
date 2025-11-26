from LifeStyle import LifeStyle
from typing import Any


class Scoped(LifeStyle):
    def __init__(self, class_type: type, params: list[str]) -> None:
        super().__init__(class_type, params)
        self._instance = None

    def create_instance(self, params: dict[str, Any] | None = None) -> Any:
        if self._instance == None:
            if self._params == []:
                self._instance = self._class_type()
                return self._instance

            elif params != None:
                self._instance = self._class_type(**params)
                return self._instance
        
        return self._instance
    