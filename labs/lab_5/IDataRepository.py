from typing import TypeVar, Sequence

T = TypeVar("T")

class IDataRepository:
    def get_all(self) -> Sequence[T]:
        ...
    
    def get_by_id(self, id: int) -> T | None:
        ...
    
    def add(self, item: T) -> None:
        ...
    
    def update(self, item: T) -> None:
        ...
    
    def delete(self, item: T) -> None:
        ...

