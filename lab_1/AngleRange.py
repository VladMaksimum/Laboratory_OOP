from Angle import Angle

class AngleRange:

    start : 'Angle'
    end : 'Angle'
    including : bool

    def __init__(self, start : Angle | int | float, end : Angle | int | float) -> None:
        if type(start) == type(Angle):
            self.start = start
        else:
            self.start = Angle(start)
        
        if type(end) == type(Angle):
            self.end = end
        else:
            self.end = Angle(end)
        
        self.including = True
    
    @classmethod
    def as_exclusion(cls, start : Angle | int | float, end : Angle | int | float) -> 'AngleRange':
        return cls(start, end)

    
    def __str__(self) -> str:
        if self.including:
            return '[' + str(self.start) + '; ' + str(self.end) + ']'
        
        return '(' + str(self.start) + '; ' + str(self.end) + ')'

    def __repr__(self) -> str:
        return str(self)
    
    def __abs__(self) -> float:
        return self.end - self.start
    



    
    def __eq__(self, other : 'AngleRange') -> bool:
        return (self.start == other.start) and (self.end == other.end) and (self.including == other.including)
    
    def __ne__(self, other : 'AngleRange') -> bool:
        return (self.start != other.start) or (self.end != other.end) or (self.including != other.including)
    
    def __lt__(self, other : 'AngleRange') -> bool:
        if abs(self) < abs(other):
            return True
        elif abs(self) == abs(other) and other.including and not self.including:
            return True
       
        return False
    
    def __le__(self, other : 'AngleRange') -> bool:
        return (self < other) or (self == other)
    
    def __gt__(self, other : 'AngleRange') -> bool:
        if abs(self) > abs(other):
            return True
        elif abs(self) == abs(other) and not other.including and self.including:
            return True
       
        return False
    
    def __ge__(self, other : 'AngleRange') -> bool:
        return (self > other) or (self == other)
    



    def is_part_of(self, other : 'AngleRange') -> bool:
        if other.including and self.start >= other.start and self.end <=other.end:
            return True
        elif self.including and self.start > other.start and self.end <other.end:
            return True
        
        return self.start >= other.start and self.end <=other.end
    
    def is_involved(self, angle : 'Angle') -> bool:
        print(type(self.start), type(self.end), type(angle))
        if self.including:
            print((self.start <= angle), (self.end >= angle))
            return (self.start <= angle) and (self.end >= angle)
        
        return (self.start < angle) and (self.end > angle)

    
    


    

    
