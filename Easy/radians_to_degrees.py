import math

def rad_to_deg(r):
    return round(math.degrees(r), 1)

r = float(input("Enter radians: "))
d = rad_to_deg(r)

print(d)
