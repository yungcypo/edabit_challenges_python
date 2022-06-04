def dis(p, d):
    return p - p * (d / 100)

p = float(input("Enter a price: "))
d = float(input("Enter a discount [%]: "))

result = dis(p, d)

print(result)
