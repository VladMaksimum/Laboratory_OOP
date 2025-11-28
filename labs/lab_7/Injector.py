from LifeStyle import LifeStyle
from typing import Any, Callable

class Injector:
    def __init__(self) -> None:
        self._depdencies: dict[type, LifeStyle | Callable] = {}
    
    def register(self, interface_type: type, class_type: type, lifestyle_type: type, params: list[str] | None = None) -> None:
        if params == None:
            params = []
        
        self._depdencies[interface_type] = lifestyle_type(class_type, params)
    
    def get_instance(self, interface_type: type, params: dict[str, Any] | None = None) -> Any:
        if interface_type in self._depdencies.keys():
            if callable(self._depdencies[interface_type]):
                return self._depdencies[interface_type]()
            
            return self._depdencies[interface_type].create_instance(params)
        else:
            raise Exception(f"Interface {interface_type.__name__} not registered")
    
    def register_fabric(self, interface_type: type, fabric_method: Callable) -> None:
        self._depdencies[interface_type] = fabric_method


