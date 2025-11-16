from IDataRepository import IDataRepository
from typing import TypeVar, Sequence, Generic
from pathlib import Path
import json

T = TypeVar("T")


class DataRepository(Generic[T], IDataRepository[T]):
    def __init__(self, rep_path: str, data_type: type) -> None:
        self._rep_path = rep_path
        self._data_type = data_type

    def get_all(self) -> Sequence[T]:
        folder  = Path(self._rep_path)
        data = []

        for file in list(map(str, folder.glob("*"))):
            with open(file) as atributes:
                obj = self._data_type(**json.load(atributes))
                data.append(obj)
        
        return data

    
    def get_by_id(self, id: int) -> T | None:
        data = self.get_all()

        for element in data:
            if element.id == id:
                return element
        
        return None

    def add(self, item: T) -> None:
        new_file = self._rep_path + "/data" + str(item.id) + ".json"

        Path(new_file).touch()
        json.dump(item.__dict__, open(new_file, "w"), indent=4)
        
    
    def update(self, item: T) -> None:
        item_file = self._rep_path + "/data" + str(item.id) + ".json"
        json.dump(item.__dict__, open(item_file, "w"), indent=4)

    def delete(self, item: T) -> None:
        Path.unlink(self._rep_path + "/data" + str(item.id) + ".json")

    
