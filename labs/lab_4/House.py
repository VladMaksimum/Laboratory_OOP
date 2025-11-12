from Event import Event
from PropertyChangedEventArgs import PropertyChangedEventArgs
from PropertyChangedEventHandler import PropetryChangedEventHandler
from PropertyChangingEventArgs import PropertyChangingEventArgs
from PropertyChangingEventHandler import PropertyChangingEventHandler
 
class House:
    def __init__(self, city: str, street: str, number: int):
        self._city = city
        self._street = street
        self._number = number
    
    def __str__(self) -> str:
        return self.__class__.__name__
    
    @property
    def city(self) -> str:
        return self._city
    
    @city.setter
    def city(self, new_city: str) -> None:
        old_value = self._city
        self._city = new_city

        Event([PropertyChangingEventHandler()]).invoke(self, PropertyChangingEventArgs("_city", old_value, new_city, False))
        Event([PropetryChangedEventHandler()]).invoke(self, PropertyChangedEventArgs("_city"))
    
    @property
    def street(self) -> str:
        return self._street
    
    @street.setter
    def street(self, new_street: str) -> None:
        old_value = self._street
        self._street = new_street

        Event([PropertyChangingEventHandler()]).invoke(self, PropertyChangingEventArgs("_street", old_value, new_street, True))
        Event([PropetryChangedEventHandler()]).invoke(self, PropertyChangedEventArgs("_street"))
    
    @property
    def number(self) -> int:
        return self._number
    
    @number.setter
    def number(self, new_number: int) -> None:
        old_value = self._number
        self._number = new_number

        Event([PropertyChangingEventHandler()]).invoke(self, PropertyChangingEventArgs("_number", old_value, new_number, True))
        Event([PropetryChangedEventHandler()]).invoke(self, PropertyChangedEventArgs("_number"))
    
    
