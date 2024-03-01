import math
a, b, c = map(int, input().split())
def angles(a, b, c):
    angle_a = int(math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))))
    return angle_a

angle_a = angles(a, b, c)
angle_b = angles(b, a, c)
angle_c = angles(c, b, a)
print(angle_a, angle_b, angle_c)