def mood(s = "neutral"):
    return "Today, I'm feeling " + s
    
s = str(input("Enter a mood (or leave empty): ")).strip()
result = mood(s)

print(result)
