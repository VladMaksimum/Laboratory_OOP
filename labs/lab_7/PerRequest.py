from LifeStyle import LifeStyle
from typing import Any


class PerRequest(LifeStyle):
    def create_instance(self, interface_type: type, params: dict[str, Any] | None = None) -> Any:
        if self._params == []:
            return self._class_type()

        elif params != None:
            return self._class_type(**params)


