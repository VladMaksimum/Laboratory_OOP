from Angle import Angle
from Angle import delta

class AngleRange:

    start : 'Angle'
    end : 'Angle'
    mode: str

    def __init__(self, start: Angle, end: Angle, mode: str) -> None:
        self.start = start
        self.end = end
        self.mode = mode


    def __str__(self) -> str:
        return f'{self.mode[0]}{self.start}, {self.end}{self.mode[1]}'

    def __repr__(self) -> str:
        return str(self)
    
    def __abs__(self) -> float:
        return self.end.measure_radians - self.start.measure_radians
    



    
    def __eq__(self, other: 'AngleRange') -> bool:
        return (self.start == other.start) and (self.end == other.end) and (self.mode == other.mode)
    
    def __ne__(self, other: 'AngleRange') -> bool:
        return not self == other
    
    def __lt__(self, other: 'AngleRange') -> bool:
        if abs(self) < abs(other):
            return True
        elif abs(self) == abs(other) and self.mode < other.mode:
            return True
       
        return False
    
    def __le__(self, other: 'AngleRange') -> bool:
        return (self < other) or (self == other)
    
    def __gt__(self, other: 'AngleRange') -> bool:
        if abs(self) > abs(other):
            return True
        elif abs(self) == abs(other) and self.mode > other.mode:
            return True
       
        return False
    
    def __ge__(self, other: 'AngleRange') -> bool:
        return (self > other) or (self == other)
    



    def is_part_of(self, other: 'AngleRange') -> bool:
        if self.mode < other.mode and round(self.start.measure_radians, delta) <= round(other.start.measure_radians, delta)\
        and round(self.end.measure_radians, delta) >= round(other.end.measure_radians, delta):
            return True
        elif self.mode >= other.mode and round(self.start.measure_radians, delta) < round(other.start.measure_radians, delta)\
        and round(self.end.measure_radians, delta) > round(other.end.measure_radians, delta):
            return True
        
        return False
        
        
    
    def is_involved(self, angle: 'Angle') -> bool:
        if round(self.start.measure_radians, delta) < round(angle.measure_radians, delta) \
            and round(self.end.measure_radians, delta) > round(angle.measure_radians, delta):
            return True
        
        elif (angle == self.start and self.mode[0] == '[') or (angle == self.end and self.mode[1] == ']'):
            return True
        
        return False

    
    


    

    
