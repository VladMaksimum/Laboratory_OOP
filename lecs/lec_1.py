#Protocols

from typing import Sized, Callable, Container, Any, Iterator, Collection, Protocol

class Vector3d(Sized, Callable, Container):
    def __init__(self, x : float, y : float, z : float) -> None:
        self.x = x
        self.y = y
        self.z = z
        
    #поддержка протокола Sized
    def __len__(self) -> int:
        return 3
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'
    
    #поддержка протокола Callable
    def __call__(self) -> str:
        print(self.__str__())
    
    #поддержка протокола Container
    def __contains__(self, value : float) -> bool:
        return value in ['x','y','z']
    
    #поддержка протокола Collection(iter,len,contains)
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
    


def print_lenght(v : Sized) -> int:
    print(len(v))

v1 = Vector3d(1,20,20)
v1()
print(len(v1))
print_lenght(v1)


def filter_data(lst : Collection, filtered_value : Any) -> Iterator[Any]:
    for item in lst:
        if item == filtered_value:
            yield item

for x in filter_data(v1, 20):
    print(x)

for x in filter_data('sdvj', 20):
    print(x)

for x in filter_data([1,2,3,20], 20):
    print(x)

#for x in filter_data(10, 20):
    #print(x)


class Saying_Meow(Protocol):
    def say_meow(self):
        ...

class Cat:
    def say_meow(self):
        print("MEOW!!!")

def print_voice_of_cat(sayer : Saying_Meow):
    sayer.say_meow()

cat = Cat()
print_voice_of_cat(cat)
#print_voice_of_cat(v1)


from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, text:str) -> None:
        ...

class ModernPrinter(Printer):
    def print(self, text:str) -> None:
        print(text)

printer = ModernPrinter()
printer.print("Hello.")
    
def send_doc_to_printer(text:str, printer:Printer) -> None:
    printer.print(text)

send_doc_to_printer("I printed text", printer)

#printer2 = Printer()
