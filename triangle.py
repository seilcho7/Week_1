star = 1
height = int(input("What is the height? "))

print(((" ") * (height - (star))) + (("*") * star) + ((" ") * (height - star)))
while star < height:
    print(((" ") * (height - (star + 1))) + (("*") * (star + 1) + ("*" * star) + ((" ") * (height - (star + 1)))))
    star = star + 1