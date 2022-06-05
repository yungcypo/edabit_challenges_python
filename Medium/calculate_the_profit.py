def calculate(x):
    return round(x["sell_price"] * x["inventory"] - x["cost_price"] * x["inventory"])
profit = {}

profit["cost_price"] = float(input("Enter cost price: "))
profit["sell_price"] = float(input("Enter sell price: "))
profit["inventory"] = float(input("Enter quantity: "))

print(calculate(profit))
