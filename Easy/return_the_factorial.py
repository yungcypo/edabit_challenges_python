def factorial(n):
    result = 1
    for i in range(n):
        result *= (i+1)
    
    return result

n = int(input("Enter a number: "))
result = factorial(n)

print(result)
