import math

def area(r):
    return round(((r * 2) ** 2) - ((r/math.sqrt(2) * 2) ** 2), 2)

r = int(input("Enter r: "))

print(area(r))
