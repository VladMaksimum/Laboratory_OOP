# Паттерн Слушатель

from abc import ABC, abstractmethod

class DataLister(ABC):
    @abstractmethod
    def on_property_changed(self, sender: object, prop_name: str) -> None:
        ...

class SimpleDataLister(DataLister):
    def on_property_changed(self, sender: object, prop_name: str) -> None:
        print(f'property {prop_name} changed in {sender}')
        
class DataChangingLister(ABC):
    @abstractmethod
    def on_property_changing(self, sender: str, prop_name:str\
                            ,old_value: str, new_value: str) -> bool:
        ...

class WaspAddressValidator(DataChangingLister):
    def on_property_changing(self, sender: str, prop_name:str\
                            ,old_value: str, new_value: str) -> bool:
        if prop_name != "address":
            return True
        
        return "pole" in new_value.lower()

class DataPropertyChangedMinin:
    def __init__(self):
        self.data_listers = []
        self.validators = []
    
    def add_lister(self, lister: DataLister) -> None:
        self.data_listers.append(lister)
        
    def del_lister(self, lister: DataLister) -> None:
        self.data_listers.remove(lister)
    
    def add_validator(self, validator: DataChangingLister) -> None:
        self.validators.append(validator)
        
    def del_validator(self, validator: DataChangingLister) -> None:
        self.validators.remove(validator)

    def notify_data_listers(self, prop_name: str) -> None:
        for lister in self.data_listers:
            lister.on_property_changed(self, prop_name)
    
    def notify_validators(self, old_value, new_value) -> bool:
        for validator in self.validators:
            if not validator.on_property_changing(self, prop_name, old_value, new_value):
                print("Validator blocked operation")
                return False
            
        return True
    
class NotifyDataChanging:
    def __init__(self):
        DataPropertyChangedMinin.__init__(self)
    
    def __setattr__(self, prop_name: str, value: object) -> None:
        if prop_name in ["self.data_listers", "self.validators"]:
            super().__setattribute__(prop_name, value)
            return
        
        old_value = self.__getattribute__(prop_name)
        
        if not self.notify_validators(prop_name, old_value, value):
            return
        
        super().__setattribute__(prop_name, value)
        
        self.notify_data_listers(prop_name)
    


class Wasp(NotifyDataChanging):
    def __init__(self, name: str, address: str) -> None:
        super().__init__()
        self.data_listers = []
        self.validators = []
        self.name = name
        self._address = address
    '''
    def add_lister(self, lister: DataLister) -> None:
        self.data_listers.append(lister)
        
    def del_lister(self, lister: DataLister) -> None:
        self.data_listers.remove(lister)
    
    def add_validator(self, validator: DataChangingLister) -> None:
        self.validators.append(validator)
        
    def del_validator(self, validator: DataChangingLister) -> None:
        self.validators.remove(validator)
     '''   
    @property
    def address(self) -> str:
        return self._address
    '''
    @address.setter
    def address(self, address: str) -> None:
        #for validator in self.validators:
         #   if not validator.on_property_changing(self, "address", self.address, address):
          #      return
        if not self.notify_validators(self.address, address):
            return
        
        self._address = address
        
        self.notify_data_listers(prop_name)
        
        #for lister in self.data_listers:
         #   lister.on_property_changed(self, "address")
        
        #print("Address is set")
    '''
    '''
    def notify_data_listers(self, prop_name: str) -> None:
        for lister in self.data_listers:
            lister.on_property_changed(self, prop_name)
    
    def notify_validators(self, old_value, new_value) -> bool:
        for validator in self.validators:
            if not validator.on_property_changing(self, prop_name, old_value, new_value):
                print("Validator blocked operation")
                return False
            
        return True
    
    '''
    @property
    def name(self):
        return name
    
    @address.setter
    def name(self, name: str) -> None:
        if not self.notify_validators(self.name, name):
            return
        
        self.name = name
        self.notify_data_listers(prop_name)
    
    
    def __str__(self) -> None:
        return (f'{type(self).__name__} name: {self.name} address: {self.address}')
'''
    def __setattr__(self, prop_name: str, value: object) -> None:
        if prop_name in ["self.data_listers", "self.validators"]:
            super().__setattribute__(prop_name, value)
            return
        
        old_value = self.__getattribute__(prop_name)
        
        if not self.notify_validators(prop_name, old_value, value):
            return
        
        super().__setattribute__(prop_name, value)
        
        self.notify_data_listers(prop_name)
        '''
wasp1 = Wasp(name="Masha", address="Pole 3, Nora 4")
lister = SimpleDataLister()
validator1 = WaspAddressValidator()
wasp1.add_lister(lister)
wasp1.add_validator(validator1)

wasp1.address = "Pole 1, Nora 666"
print(wasp1.address)
