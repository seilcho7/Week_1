name = input("What is your name? ")
print("%s, %s!" % ("Hello", name))

name_upper = input("What is your name? ".upper())
print("%s, %s!" % ("Hello".upper(), name.upper()))
print("Your name has ".upper() + str(len(name_upper))
+ " letters in it! awesome!".upper())