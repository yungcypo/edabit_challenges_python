def damage(a, i, p):
    if p == "second" or p == "s":
        return a * i
    elif p == "minute" or p == "m":
        return a * i * 60
    elif p == "hour" or p == "h":
        return a * i * 3600

a = int(input("Enter amount of damage: "))
i = int(input("Enter time interval: "))  # how many times per time period (5/s, 4/min, 7/h, ...)
p = str(input("Enter time period (s, m, h): "))

result = damage(a, i, p)

print(result)
