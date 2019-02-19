total = float(input("Total bill amount? "))
service = input("Level of service? ")
tip = 0
if service == "good":
    tip = float(total) * 0.2
elif service == "fair":
    tip = float(total) * 0.15
elif service == "bad":
    tip = float(total) * 0.1
else:
    print("good, fair, or bad")
total_amount = total + tip
print("Tip amount: $%.2f\nTotal amount: $%.2f" % (tip, total_amount))