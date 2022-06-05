def area(x):
    return round((x["area"] / total) * 100, 2)

total = 148940000
country = {}

country["name"] = str(input("Enter name of a country: "))
country["area"] = int(input("Enter area of " + country["name"] + " [km²]: "))

print(country["name"] + " is " + str(area(country)) + "% of total world's landmass")
