from unittest import result


def luke(s):
    result = ""
    if s == "darth wader":
        result = "father"
    elif s == "leia":
        result = "sister"
    elif s == "han":
        result = "brother in law"
    elif s == "r2d2":
        result = "driod"
    else:
        return "Invalid input"

    return "Luke, I'm your " + result + "."

s = str(input("Enter name: ")).lower()
result = luke(s)

print(result)
