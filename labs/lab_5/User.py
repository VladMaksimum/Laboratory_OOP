from dataclasses import dataclass
from typing import Self


@dataclass
class User:
    id: int
    name: str
    login: str
    password: str
    address: str
    email: str = None

    def __lt__(self, other: Self) -> bool:
        return self.name < other.name
    
    def __gt__(self, other: Self) -> bool:
        return self.name > other.name
    



