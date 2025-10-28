from AngleRange import AngleRange
from Angle import Angle
import math

print("Angle tests:")

angle1 = Angle(math.pi/6)
print("Angle1 =", int(angle1), "degrees")
angle2 = Angle.from_degrees(120)
print("Angle2 =", int(angle2), "degrees")
angle3 = Angle(math.pi*8/3)
print("Angle3 =", int(angle3), "degrees")

print()
print(int(angle1), "degrees angle is less than", int(angle2), "degrees angle?", angle1 < angle2)
print(int(angle3), "degrees angle is more than", int(angle1), "degrees angle?", angle3 > angle1)
print(int(angle2), "degrees angle is equal", int(angle3), "degrees angle?", angle2 == angle3)

print()
angle4 = Angle.from_degrees(180)
print("Angle4 =", int(angle4), "degrees")
print("Changing...")
angle4.measure_degrees = 140
print("Now angle4 =", int(angle4), "degrees")

print()
print("Angle", int(angle1), "degress + angle", int(angle3), "degrees =", int(angle1 + angle3), "degrees")
print("Angle", int(angle3), "degress *", 4, " =", int(angle3 * 4), "degrees\n")



print("Range tests:")

test1 = AngleRange(angle1, angle2, "[]")
print("Range1 =", test1)
test2 = AngleRange(angle1, angle2, '[)')
print("Range2 =", test2)
test3 = AngleRange(angle2, angle3, "()")
print("Range3 =", test3)
test4 = AngleRange(angle1, angle2, '(]')
print("Range4 =", test4)
test5 = AngleRange(Angle.from_degrees(60), Angle.from_degrees(180), "()")
print("Range5 =", test5)
test6 = AngleRange(Angle.from_degrees(140), Angle.from_degrees(180), "[]")
print("Range6 =", test6)
test7 = AngleRange(Angle.from_degrees(60), Angle.from_degrees(90), "()")
print("Range7 =", test7)

print()
print(test2, "is part of", test1, "?", test2.is_part_of(test1))
print(test1, "is part of", test2, "?", test1.is_part_of(test2))
print(test3, "is part of", test1, "?", test3.is_part_of(test1))
print(test4, "is part of", test2, "?", test4.is_part_of(test2))
print(test5, "is part of", test1, "?", test5.is_part_of(test1))

print()
print(int(angle2), "in", test2, "?", test2.is_involved(angle2))
print(int(angle2), "in", test1, "?", test1.is_involved(angle2))

print()
print(test1, "+", test2, '=', " ".join(map(str, test1 + test2)))
print(test3, "+", test4, '=', " ".join(map(str, test3 + test4)))
print(test2, "+", test4, '=', " ".join(map(str, test2 + test4)))
print(test3, "+", test5, '=', " ".join(map(str, test3 + test5)))
print(test6, "+", test2, '=', " ".join(map(str, test6 + test2)))

print()
print(test3, "-", test5, "=", " ".join(map(str, test3 - test5)))
print(test1, "-", test2, "=", " ".join(map(str, test1 - test2)))
print(test1, "-", test7, "=", " ".join(map(str, test1 - test7)))
print(test6, "-", test7, "=", " ".join(map(str, test6 - test7)))