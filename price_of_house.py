price = 1000000
print(type(price))

good_credit = input("Do you have good credit?(y/n):")

if good_credit == "y":
    down_payment = 0.1 * price
    print(f"Down payment: {down_payment}")
else:
    down_payment = 0.2 * price
    print(f"Down payment: {down_payment}")
