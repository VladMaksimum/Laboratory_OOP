# паттерн сингтон

class SingleTon1:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        
        return cls._instance


obj1 = SingleTon1()
obj2 = SingleTon1()
print(obj1)
print(obj2)
print(obj1 == obj2)


class MySingleTon(SingleTon1): # не предпочтительное использование
    pass


class SingleTonMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if SingleTonMeta._instance is None:
            SingleTonMeta._instance = super().__call__(cls, *args, **kwargs)
        
        return _instance

class MySingleTonClass(metaclass=SingleTonMeta):
    pass

'''
#obj1 = MySingleTonClass()
obj2 = MySingleTonClass()
print(obj1)
print(obj2)
print(obj1 == obj2)
'''

def singleton(cls):
    _instance = None

    def wrapper(*args, **kwargs):
        nonlocal _instance
        if _instance == None:
            _instance = cls(*args, **kwargs)
        
        return _instance

    return wrapper

@singleton
class MySIngleDcor:
    pass

obj1 = MySIngleDcor()
obj2 = MySIngleDcor()
print(obj1)
print(obj2)
print(obj1 == obj2)


def singletonjmany(n_max):
    n_current = 0

    def singleton(cls):
        _instance = None

        def wrapper(*args, **kwargs):
            nonlocal _instance, n_current
            if _instance == None or n_current < n_max:
                _instance = cls(*args, **kwargs)
                n_current += 1
            return _instance
            
        return wrapper

    return singleton

@singletonjmany(n_max=3)
class MyClass():
    pass

obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()
obj4 = MyClass()
obj5 = MyClass()

print(obj1)
print(obj2)
print(obj3)
print(obj4)
print(obj5)

print(obj4 == obj5)

from my_module import my_single

