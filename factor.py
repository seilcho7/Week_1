number = int(input("Number?: "))

start_number = 1

while start_number <= number:
    if number % start_number == 0:
        print(start_number)
    

    start_number = start_number + 1