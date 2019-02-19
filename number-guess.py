the_magic_number = 7

user_input = int(input("Enter a number between 1 and 10: "))

if user_input == the_magic_number:
    print("Yay you did it!")
elif user_input < 1 or user_input > 10:
    print("Over the line!")
else:
    print("Boo. That is not right. Go home.")
