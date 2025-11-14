from DataRepository import DataRepository
from User import User
from pathlib import Path
import json

class UserRepository(DataRepository[User]):
    def get_by_login(self, login: str) -> User | None:
        for element in self._data:
            if element.login == login:
                return element
        
        return None