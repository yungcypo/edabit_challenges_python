def snakefill(n):
    a = 1
    s = -1
    while True:
        if n ** 2 > a:
            a *= 2
            s += 1
        else:
            return s

n = int(input("Enter n: "))

print(snakefill(n))
