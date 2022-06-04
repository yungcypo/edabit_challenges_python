'''
If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.
'''

def curson(n):
    return (2 ** n + 1) % (2 * n + 1) == 0

n = int(input("Enter a number: "))
result = curson(n)

print(result)
