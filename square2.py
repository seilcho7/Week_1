# star = 0

# size = int(input("How big is the square? "))

# while star < size:
#     print(("*") * size)
#     star = star + 1

num_of_lines = int(input("How big is the square?"))

def Squarysquare(numb):
    placey_place = ""
    lines = 0
    while lines < numb:
        lines = lines + 1
        placey_place += ("*" * numb) + "\n"
    return placey_place.rstrip()

print(Squarysquare(num_of_lines))