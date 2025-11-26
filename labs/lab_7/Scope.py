from typing import Self
from Injector import Injector
from Scoped import Scoped

class Scope:
    def __init__(self, injector: Injector) -> None:
        self._injector = injector

    def get_all_scoped(self) -> list[Scoped]:
        all_scoped = []

        for interface, lifestyle in self._injector._depdencies.items():
            if isinstance(lifestyle, Scoped):
                all_scoped.append(lifestyle)
        
        return all_scoped
    
    def remove_instances(self, scoped_lst: list[Scoped]) -> None:
        for cls in scoped_lst:
            cls._instance = None

    def __enter__(self) -> Self:
        self.remove_instances(self.get_all_scoped())
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.remove_instances(self.get_all_scoped())
        