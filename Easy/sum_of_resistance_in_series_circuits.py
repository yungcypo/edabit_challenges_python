def sum(a):
    result = 0
    for i in a:
        result += i
    
    return result

a = []

while True:
    b = float(input("Enter a number (enter 0 to exit): "))
    if b != 0:
        a.append(b)
    else: 
        break

result = sum(a)
print(result)
