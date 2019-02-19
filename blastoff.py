import time

user_input = int(input("Numbers?: "))
while user_input > 20:
    print("Numbers cannot be bigger than 20")
    user_input = int(input("Numbers?: "))


dec_number = user_input
number = 0

while number <= user_input:
    print(dec_number)
    dec_number = user_input - (number + 1)
    number += 1
    time.sleep(1)

print("This is the end")


# import time

# starting_number = int(input("starting number? "))
# i = 0
# while i < starting_number:
#   print(starting_number - i)
#   i = i + 1  
#   time.sleep(1)