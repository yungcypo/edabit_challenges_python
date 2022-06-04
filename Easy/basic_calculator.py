def calc(a, o, b):
    if o == "+":
        return a + b
    elif o == "-":
        return a - b
    elif o == "*":
        return a * b
    elif o == "/":
        return a / b 

    return 0

a = float(input("Enter first number: "))
o = str(input("Enter a operator: "))
b = float(input("Enter second number: "))

result = calc(a, o, b)

print(result)
