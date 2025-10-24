from AngleRange import AngleRange
from Angle import Angle
import math

angle1 = Angle(math.pi/6)
print("Create angle1:", int(angle1), "degrees")
angle2 = Angle.from_degrees(120)
print("Create angle2:", int(angle2), "degrees")
angle3 = Angle(math.pi*8/3)
print("Angle1 in radians:", angle1)
print("Angle3 in radians:", angle3)

print(int(angle2), "degrees angle is equal", int(angle3), "degrees angle?", angle2 == angle3)


test1 = AngleRange(angle1, angle2, "[]")
print("Create test range1:", test1)

test2 = AngleRange(angle1, angle2, '[)')
print(test2, "is part of", test1, "?", test2.is_part_of(test1))
print(test1, "is part of", test2, "?", test1.is_part_of(test2))

test3 = AngleRange(angle2, angle3, "()")
print(test3, "is part of", test1, "?", test3.is_part_of(test1))

print(int(angle2), "in", test2, "?", test2.is_involved(angle2))
print(int(angle2), "in", test1, "?", test1.is_involved(angle2))

test4 = AngleRange(angle1, angle2, '(]')
print(test4, "is part of", test2, "?", test4.is_part_of(test2))

test5 = AngleRange(Angle.from_degrees(60), Angle.from_degrees(90), "()")
print(test5, "is part of", test1, "?", test5.is_part_of(test1))

