while True:
    try:
        total = float(input("Total bill amount? "))
    except:
        print("Enter numbers")
    else:
        break

service = input("Level of service? ")

while service != "good" and service != "fair" and service != "bad":
    print("Enter good, fair, or bad")
    service = input("Level of service? ")


while True:
    try:
        split = float(input("Split how many ways? "))
    except:
        print("Enter numbers")
    else:
        break

tip = 0
total_amount = 0

if service == "good":
    tip = float(total) * 0.2
elif service == "fair":
    tip = float(total) * 0.15
elif service == "bad":
    tip = float(total) * 0.1

total_amount = total + tip
amount_per_person = total_amount / split
print("Tip amount: $%.2f\nTotal amount: $%.2f\nAmount per person: $%.2f" % (tip, total_amount, amount_per_person))