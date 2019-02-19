import random

secret_number = random.randint(1, 10)
trys = 0

print("I am thinking of a number between 1 and 10.")

while trys < 5:
    try:
        print("You have " + str(5 - trys) + " guesses left.")
        number = int(input("What's the number? "))
        if number == secret_number:
            print("Yes! You win!")
            trys = 5
            cont = input("Do you want to play again (Y or N)? ").upper()
            if cont == "Y":
                trys = 0
            elif cont == "N":
                print("Bye!")
                break
        elif number < secret_number:
            trys += 1
            print("%d is too low." % (number))
        elif number > secret_number:
            trys += 1
            print("%d is too high." % (number))
        while trys == 5:
            print("You ran out of guesses!")
            cont = input("Do you want to play again (Y or N)? ").upper()
            if cont == "Y":
                trys = 0
            elif cont == "N":
                print("Bye!")
                break
    except:
        pass