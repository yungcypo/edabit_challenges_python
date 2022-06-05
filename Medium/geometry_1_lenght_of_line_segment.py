import math

def lenght(line):
    x = abs(line[0][0] - line[1][0])
    y = abs(line[0][1] - line[1][1])
    
    return round(math.sqrt(x ** 2 + y ** 2), 2)

line = [[int, int],[int, int]]

line[0][0] = int(input("X coordinate of start: "))
line[0][1] = int(input("Y coordinate of start: "))
print()
line[1][0] = int(input("X coordinate of end: "))
line[1][1] = int(input("Y coordinate of end: "))
print()

print(lenght(line))
