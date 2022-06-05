def fizzbuzz(x):
    result = ""
    if x % 3 == 0:
        result += "Fizz"
    if x % 5 == 0:
        result += "Buzz"
    return result

x = int(input("Enter a number: "))

print(fizzbuzz(x))
