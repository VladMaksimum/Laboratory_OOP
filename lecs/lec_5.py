# Сериализация (паттерн мементо)

class Toud:
    def __init__(self, name: str, address: str, child: Self) -> None:
        self.name= name
        self.address = address
        self.child = child
        self.state_saver = StateSaver(self)
        
        def support_serialization(self) -> StateSaver:
            return self.state_saver
    
    def to_dict(self) -> Dict[str, Any]:
        return {'name': self.name, \
                'address': self.address, \
                "child": self.child.to_dict()}
    

class StateSaver:
    def __init__(self, object_to_save: object) -> None:
        self.object_to_save = object_to_save
    
    def to_dict(self) -> Dict[str, Any]: #неизменяем этот метод
        ...
    
    def is_serializable(self, prop_name: str) -> None: # реализуем под класс
        ...
    
    def get_serializable_name(self, prop_name: str) -> None:
        ...

