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
        return f'{self.mode[0]}{int(self.start)}, {int(self.end)}{self.mode[1]}'

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
        if self == other:
            return True
    
        match self.mode:
            case "[]":
                match other.mode:
                    case "[]":
                        return (round(self.start.measure_radians, delta) >= round(other.start.measure_radians, delta)\
                            and round(self.end.measure_radians, delta) <= round(other.end.measure_radians, delta))
                    case "[)":
                        return (round(self.start.measure_radians, delta) >= round(other.start.measure_radians, delta)\
                            and round(self.end.measure_radians, delta) < round(other.end.measure_radians, delta))
                    case "(]":
                        return (round(self.start.measure_radians, delta) > round(other.start.measure_radians, delta)\
                            and round(self.end.measure_radians, delta) <= round(other.end.measure_radians, delta))
                    case "()":
                        return (round(self.start.measure_radians, delta) > round(other.start.measure_radians, delta)\
                            and round(self.end.measure_radians, delta) < round(other.end.measure_radians, delta))
            case "[)":
                match other.mode:
                    case "[]":
                        return (round(self.start.measure_radians, delta) >= round(other.start.measure_radians, delta)\
                            and round(self.end.measure_radians, delta) <= round(other.end.measure_radians, delta))
                    case "[)":
                        return (round(self.start.measure_radians, delta) >= round(other.start.measure_radians, delta)\
                            and round(self.end.measure_radians, delta) <= round(other.end.measure_radians, delta))
                    case "(]":
                        return (round(self.start.measure_radians, delta) > round(other.start.measure_radians, delta)\
                            and round(self.end.measure_radians, delta) <= round(other.end.measure_radians, delta))
                    case "()":
                        return (round(self.start.measure_radians, delta) > round(other.start.measure_radians, delta)\
                            and round(self.end.measure_radians, delta) <= round(other.end.measure_radians, delta))
            case "(]":
                match other.mode:
                    case "[]":
                        return (round(self.start.measure_radians, delta) >= round(other.start.measure_radians, delta)\
                            and round(self.end.measure_radians, delta) <= round(other.end.measure_radians, delta))
                    case "[)":
                        return (round(self.start.measure_radians, delta) >= round(other.start.measure_radians, delta)\
                            and round(self.end.measure_radians, delta) < round(other.end.measure_radians, delta))
                    case "(]":
                        return (round(self.start.measure_radians, delta) >= round(other.start.measure_radians, delta)\
                            and round(self.end.measure_radians, delta) <= round(other.end.measure_radians, delta))
                    case "()":
                        return (round(self.start.measure_radians, delta) >= round(other.start.measure_radians, delta)\
                            and round(self.end.measure_radians, delta) < round(other.end.measure_radians, delta))
            case "()":
                match other.mode:
                    case "[]":
                        return (round(self.start.measure_radians, delta) >= round(other.start.measure_radians, delta)\
                            and round(self.end.measure_radians, delta) <= round(other.end.measure_radians, delta))
                    case "[)":
                        return (round(self.start.measure_radians, delta) >= round(other.start.measure_radians, delta)\
                            and round(self.end.measure_radians, delta) <= round(other.end.measure_radians, delta))
                    case "(]":
                        return (round(self.start.measure_radians, delta) >= round(other.start.measure_radians, delta)\
                            and round(self.end.measure_radians, delta) <= round(other.end.measure_radians, delta))
                    case "()":
                        return (round(self.start.measure_radians, delta) >= round(other.start.measure_radians, delta)\
                            and round(self.end.measure_radians, delta) <= round(other.end.measure_radians, delta))
        
        
    
    def is_involved(self, angle: 'Angle') -> bool:
        if round(self.start.measure_radians, delta) < round(angle.measure_radians, delta) \
            and round(self.end.measure_radians, delta) > round(angle.measure_radians, delta):
            return True
        
        elif (angle == self.start and self.mode[0] == '[') or (angle == self.end and self.mode[1] == ']'):
            return True
        
        return False

    
    def __add__(self, other: 'AngleRange') -> list['AngleRange']:
        #Пересечение по одной точке
        if self.end.equal(other.start):
            if self.mode[1] == ')' and other.mode[0] == '(':
                return [self, other]
            
            return [AngleRange(self.start, other.end, self.mode[0] + other.mode[1])]
        #Симметрично
        if other.end.equal(self.start):
            if other.mode[1] == ')' and self.mode[0] == '(':
                return [other, self]
            
            return [AngleRange(other.start, self.end, other.mode[0] + self.mode[1])]
        #Не пересекаются
        if self.end.less(other.start):
            return [self, other]
        if other.end.less(self.start):
            return [other, self]
        
        #Один внутри другого
        if self.start.less(other.start) and self.end.more(other.end):
            return [self]
        if other.start.less(self.start) and other.end.more(self.end):
            return [other]
        
        #Совпали начала
        if self.start.equal(other.start):
            if ord(self.mode[0]) < ord(other.mode[0]):
                if self.end.less(other.end):
                    return [AngleRange(self.start, other.end, other.mode)]
                elif self.end.more(other.end):
                    return [AngleRange(self.start, self.end, other.mode[0] + self.mode[1])]
                elif self.end.equal(other.end):
                    if ord(self.mode[1]) < ord(other.mode[1]): 
                        return [AngleRange(self.start, self.end, other.mode)]
                    else:
                        return [AngleRange(self.start, self.end, other.mode[0] + self.mode[1])]
            else:
                if self.end.less(other.end):
                    return [AngleRange(self.start, other.end, self.mode[0] + other.mode[1])]
                elif self.end.more(other.end):
                    return [AngleRange(self.start, self.end, self.mode)]
                elif self.end.equal(other.end):
                    if ord(self.mode[1]) < ord(other.mode[1]): 
                        return [AngleRange(self.start, self.end, self.mode[0] + other.mode[1])]
                    else:
                        return [AngleRange(self.start, self.end, self.mode)]
        #Совпали концы
        elif self.end.equal(other.end):
            if ord(self.mode[1]) < ord(other.mode[1]):
                if self.start.less(other.start):
                    return [AngleRange(self.start, other.end, self.mode[0] + other.mode[1])]
                elif self.start.more(other.start):
                    return [AngleRange(other.start, self.end, other.mode[0] + other.mode[1])]
            else:
                if self.start.less(other.start):
                    return [AngleRange(self.start, other.end, self.mode[0] + self.mode[1])]
                elif self.end.more(other.end):
                    return [AngleRange(other.start, self.end, other.mode[0] + self.mode[1])]
                
        
        if self.start.equal(other.start):
            if ord(self.mode[0]) < ord(other.mode[0]):
                if self.end.less(other.end):
                    return [AngleRange(self.start, other.end, other.mode)]
                elif self.end.more(other.end):
                    return [AngleRange(self.start, self.end, other.mode[0] + self.mode[1])]
                elif self.end.equal(other.end):
                    if ord(self.mode[1]) < ord(other.mode[1]): 
                        return [AngleRange(self.start, self.end, other.mode)]
                    else:
                        return [AngleRange(self.start, self.end, other.mode[0] + self.mode[1])]
            else:
                if self.end.less(other.end):
                    return [AngleRange(self.start, other.end, self.mode[0] + other.mode[1])]
                elif self.end.more(other.end):
                    return [AngleRange(self.start, self.end, self.mode)]
                elif self.end.equal(other.end):
                    if ord(self.mode[1]) < ord(other.mode[1]): 
                        return [AngleRange(self.start, self.end, self.mode[0] + other.mode[1])]
                    else:
                        return [AngleRange(self.start, self.end, self.mode)]
        
        elif self.end.equal(other.end):
            if ord(self.mode[1]) < ord(other.mode[1]):
                if self.start.less(other.start):
                    return [AngleRange(self.start, other.end, self.mode[0] + other.mode[1])]
                elif self.start.more(other.start):
                    return [AngleRange(other.start, self.end, other.mode[0] + other.mode[1])]
            else:
                if self.start.less(other.start):
                    return [AngleRange(self.start, other.end, self.mode[0] + self.mode[1])]
                elif self.end.more(other.end):
                    return [AngleRange(other.start, self.end, other.mode[0] + self.mode[1])]
                
        
        #Пересечение
        if self.start.more(other.start) and other.start.less(self.end):
            return [AngleRange(other.start, self.end, other.mode[0] + self.mode[1])]
        if other.start.more(self.start) and self.start.less(other.end):
            return [AngleRange(self.start, other.end, self.mode[0] + other.mode[1])]

    def __sub__(self, other: 'AngleRange') -> list['AngleRange']:
        if self.end.less(other.start) or self.start.more(other.end):
            return [self]
        
        if self.end.equal(other.start):
            if (self.mode[1] == "]" and other.mode[0] == '['):
                return [AngleRange(self.start, self.end, self.mode[0] + ")")]
            
            return [self]
        
        if self.start.equal(other.end):
            if (self.mode[0] == "[" and other.mode[1] == ']'):
                return [AngleRange(self.start, self.end, "(" + self.mode[1])]
            
            return [self]
        
        
        
        if self.start.less(other.start) and self.end.more(other.end):
            range1 = AngleRange(self.start, other.start, self.mode[0] + ")")
            range2 = AngleRange(other.end, self.end, "(" + self.mode[1])

            if other.mode[0] == "(":
                range1.mode = self.mode[0] + "]"
            if other.mode[1] == ")":
                range2.mode = "[" + self.mode[1]

            return [range1, range2]
        
        if self.start.equal(other.start):
            if other.mode[0] == "(" and self.mode[0] == "[":
                if other.end.less(self.end):
                    if other.mode[1] == "]":
                        return [AngleRange(self.start, self.start, "[]"), AngleRange(other.end, self.end, "(" + self.mode[1])]
                    return [AngleRange(self.start, self.start, "[]"), AngleRange(other.end, self.end, "[" + self.mode[1])]
                elif other.end.more(self.end):
                    return [AngleRange(self.start, self.start, "[]")]
                elif other.end.equal(self.end):
                    if other.mode[1] == ")" and self.mode[1] == "]":
                        [AngleRange(self.start, self.start, "[]"), AngleRange(self.end, self.end, "[]")]
                    return [AngleRange(self.start, self.start, "[]")]
            else:
                if other.end.less(self.end):
                    if other.mode[1] == "]":
                        return [AngleRange(other.end, self.end, "(" + self.mode[1])]
                    return [AngleRange(other.end, self.end, "[" + self.mode[1])]
                elif other.end.more(self.end):
                    return []
                elif other.end.equal(self.end):
                    if other.mode[1] == ")" and self.mode[1] == "]":
                        return [AngleRange(self.end, self.end, "[]")]
                    return []
            

        if self.end.equal(other.end):
            if other.mode[1] == ")" and self.mode[1] == "]":
                if other.start.more(self.start):
                    if other.mode[0] == "[":
                        return [AngleRange(self.start, other.start, self.mode[0] + ")"), AngleRange(self.end, self.end, "[]")]
                    return [AngleRange(self.start, other.start, self.mode[0] + "]"), AngleRange(self.end, self.end, "[]")]
                elif other.start.less(self.start):
                    return [AngleRange(self.end, self.end, "[]")]
            

        if self.start.less(other.start) and self.end.more(other.start):
            if other.mode[0] == "[":
                return [AngleRange(self.start, other.start, self.mode[0] + ")")]
            return [AngleRange(self.start, other.start, self.mode[0] + "]")]
        if self.start.less(other.end) and self.end.more(other.end):
            if other.mode[1] == ']':
                return [AngleRange(other.end, self.end, "(" + self.mode[1])]
            return [AngleRange(other.end, self.end, "[" + self.mode[1])]
                

            
