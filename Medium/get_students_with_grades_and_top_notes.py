def top_note(x):
    return {
        "name" : x["name"],
        "top_note" : max(x["notes"])
    }

student = {
    "name" : "",
    "notes" : [],
}

student["name"] = str(input("Enter name: "))
while True:
    n = int(input("Enter notes (enter 0 to exit): "))
    if n != 0:
        student["notes"].append(n)
    else: 
        break

student = top_note(student)

print(student)
