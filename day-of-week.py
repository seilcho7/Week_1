day = int(input("Day (0-6)? "))
day_of_week = ""
if day == 0:
    day_of_week = "Sunday"
elif day == 1:
    day_of_week = "Monday"
elif day == 2:
    day_of_week = "Tuesday"
elif day == 3:
    day_of_week = "Wednsday"
elif day == 4:
    day_of_week = "Thursday"
elif day == 5:
    day_of_week = "Friday"    
else:
    day_of_week = "Saturday"

print(day_of_week)

if day == 0 or day == 6:
    print("Sleep in")
else:
    print("Go to work")