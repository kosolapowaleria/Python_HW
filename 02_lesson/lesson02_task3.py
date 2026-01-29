import math

def square(side):
    area = side ** 2
    return math.ceil(area)

print(square(5))