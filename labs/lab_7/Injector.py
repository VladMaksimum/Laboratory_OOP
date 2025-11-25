from LifeStyle import LifeStyle
from typing import Any, List

class Injector:
    def __init__(self) -> None:
        self._depdencies: dict[type, tuple[type, LifeStyle, list[str], int]] = {}
    
    def register(self, interface_type: type, class_type: type, lifestyle: LifeStyle, params: list[str] | None = None) -> None:
        if params == None:
            params = []

        self._depdencies[interface_type] = (class_type, lifestyle, params, 0)
    
    def create_instance(self, interface_type: type, params) -> Any:
        if self._depdencies[interface_type][2] == []:
            return self._depdencies[interface_type][0]()

        return self._depdencies[interface_type][0](**params)
    
    def get_instance(self, interface_type: type, params: dict[str, Any]) -> Any:
        if self._depdencies[interface_type][1].value == LifeStyle.PER_REQUEST.value:
            return self.create_instance(interface_type, params)
        
        elif self._depdencies[interface_type][1].value == LifeStyle.SINGLETON.value:
            if self._depdencies[interface_type][3] == 0:
                return self.create_instance(interface_type, params)
        
        elif self._depdencies[interface_type][1].value == LifeStyle.SCOPED.value:
            self._depdencies[interface_type][0]


