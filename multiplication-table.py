num_one = 1
num_two = 1
max_num = 10

while num_one <= max_num:
    while num_two <= max_num:
        multiply = num_one * num_two
        print("%d X %d = %d" % (num_one, num_two, multiply))
        num_two += 1
    num_two = 1
    num_one += 1