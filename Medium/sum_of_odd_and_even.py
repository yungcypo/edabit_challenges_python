def sum_of_odd_and_even(x):
    result = [0, 0]
    for i in x:
        if i % 2:
            result[1] += i
        else: 
            result[0] += i
    return result

x = []

while True:
    a = int(input("Enter a number (enter 0 to exit): "))
    if a != 0:
        x.append(a)
    else:
        break

print(sum_of_odd_and_even(x))
