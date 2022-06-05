# DD/MM/YYYY to YYYYMMD

def format_date(x):
    return x[-4:] + x[3:5] + x[:2]

x = str(input("Enter date (DD/MM/YYYY): "))

print(format_date(x))
