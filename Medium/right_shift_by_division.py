import math

# 80 >> 3 = floor(80/2^3) = floor(80/8) = 10

def shift_to_right(x, y):
    return math.floor(x / (2 ** y))

x = int(input("Enter X: "))
y = int(input("Enter Y: "))
z = shift_to_right(x, y)

print(z)
