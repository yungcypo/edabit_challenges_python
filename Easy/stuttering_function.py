def stuttering(s):
    result = ""
    for i in range(2):
        result += s[:2]
        result += "... "
    result += s 
    result += "?"

    return result

s = str(input("Enter a sentence: "))
a = stuttering(s)

print(a)
