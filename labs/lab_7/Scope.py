from typing import Any, Self

class Scope:
    def __init__(self) -> None:
        self._obj_list: list[Any] = []


    def __enter__(self) -> Self:
        return self

    def __exit__(self) -> None:
        pass