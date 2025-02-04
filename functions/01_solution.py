import math

def solution(radius = 10):
    area = math.pi * radius ** 2
    area = round(area, 2)
    circumference = 2 * math.pi * radius
    circumference = round(circumference, 2)
    return area , circumference

a ,b =solution()

print(a, b)