my_bag = []
my_bag.append("katana")
my_bag.append("nunchucks")
my_bag.append("calzone")
my_bag.append("bo staff")
my_bag.remove("calzone")


# print(my_bag[0])
# print(my_bag[1])

index = 0
while index < len(my_bag):
    print(my_bag[index])
    index += 1

if "calzon" in my_bag:
    print("nom nom nom")
else:
    print("I am hungry")
