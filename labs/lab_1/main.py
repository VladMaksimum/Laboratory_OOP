from AngleRange import AngleRange
from Angle import Angle

angle1 = Angle.from_degrees(30)
angle2 = Angle.from_degrees(180)

test = AngleRange(angle1, angle2)

angle3 = Angle.from_degrees(30)
angle4 = Angle.from_degrees(530)
test1 = AngleRange(angle3, angle4)


print(test, test1)
print(test1.is_part_of(test))
