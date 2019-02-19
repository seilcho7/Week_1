coins = 0

no_stop = True

while no_stop:
    print("You have %d coins." % (coins))
    ask_coins = input("Do you want another? ")
    if ask_coins == "yes":
        coins = coins + 1
    elif ask_coins =="no":
        print("Bye")
        stop = False
