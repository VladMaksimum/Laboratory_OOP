from IDataRepository import IDataRepository
from typing import TypeVar, Sequence, Generic
from pathlib import Path
import json

T = TypeVar("T")


class DataRepository(Generic[T], IDataRepository[T]):
    def __init__(self, rep_path: str) -> None:
        self._rep_path = rep_path
        self._data: list[T] = []

    def get_all(self) -> Sequence[T]:
        return self._data

    
    def get_by_id(self, id: int) -> T | None:
        for element in self._data:
            if element.id == id:
                return element
        
        return None

    def add(self, item: T) -> None:
        self._data.append(item)
        new_file = self._rep_path + "/data" + str(item.id) + ".json"

        Path(new_file).touch()
        json.dump(item.__dict__, open(new_file, "w"))
        
    
    def update(self, item: T) -> None:
        for element in self._data:
            if element.id == id:
                element = item
        
        item_file = self._rep_path + "/data" + str(item.id) + ".json"
        json.dump(item.__dict__, open(item_file, "w"))

    def delete(self, item: T) -> None:
        self._data.remove(item)

        Path.unlink(self._rep_path + "/data" + str(item.id) + ".json")

    
