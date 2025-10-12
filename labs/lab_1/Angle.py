import math

delta = 14

class Angle:

    __measure : float

    def __init__(self, radians: float) -> None:
        self.__measure = radians
    
    @classmethod
    def from_degrees(cls, degrees : float) -> 'Angle':
        return cls(degrees * math.pi/180)
    


    @property
    def measure_radians(self) -> float:
        return self.__measure
    
    @measure_radians.setter
    def measure_radians(self, value : float) -> None:
        self.__measure = value

    @property
    def measure_degrees(self) -> float:
        return (self.__measure) * 180 / math.pi
    
    @measure_degrees.setter
    def measure_degrees(self, value: float) -> None:
        self.__measure = value*math.pi/180
    

    @classmethod
    def del_extra(self, angle : 'Angle') -> float:
        measure = float(angle.measure_radians)

        while measure > 2 * math.pi:
            #print("im here")
            measure -= 2 * math.pi

        return measure

    def __eq__(self, value: 'Angle') -> bool:
        angle1 = Angle.del_extra(self)
        angle2 = Angle.del_extra(value)

        #print(angle1, angle2)
        return round(angle1, delta) == round(angle2, delta)
    
    def __ne__(self, value: 'Angle') -> bool:
        return not self == value
    
    def __lt__(self, value : 'Angle') -> bool:
        angle1 = Angle.del_extra(self)
        angle2 = Angle.del_extra(value)


        return round(angle1, delta) < round(angle2, delta)
    
    def __le__(self, value : 'Angle') -> bool:
        return self < value or self == value
    
    def __gt__(self, value : 'Angle') -> bool:
        #print("yes im dumb")
        angle1 = Angle.del_extra(self)
        angle2 = Angle.del_extra(value)

        return round(angle1, delta) > round(angle2, delta)
    
    def __ge__(self, value : 'Angle') -> bool:
        return self > value or self == value
    

    
    def __float__(self) -> float:
        return self.measure_radians
    
    def __int__(self) -> int:
        return int(round(self.measure_degrees))
    
    def __str__(self) -> str:
        return str(self.measure_radians)
    
    def __repr__(self) ->str:
        return str(self)
    

    def __add__(self, value) -> 'Angle':
        if isinstance(value, self.__class__):
            return Angle(self.measure_radians + value.measure_radians)
        elif isinstance(value, (int, float)):
            return Angle(self.measure_radians + value)
        else:
            raise TypeError
    
    def __sub__(self, value : 'Angle') -> 'Angle':
        if self.measure_radians > value.measure_radians:
            return Angle(self.measure_radians - value.measure_radians)

        return Angle(value.measure_radians - self.measure_radians)
    
    def __mul__(self, value : float) ->'Angle':
        return Angle(self.measure_radians * value)
    
    def __truediv__(self, value : float) ->'Angle':
        return Angle(self.measure_radians / value)
    


    
