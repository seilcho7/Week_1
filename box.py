width = int(input("Width? "))
height = int(input("Height? "))

star_w = 0
star_h = 0

while star_w < height:
    print(("*") * width)
    while star_h < (height - 2):
        print(("*" + ((" ") * (width - 2)) + "*"))
        star_h = star_h + 1
    star_w = star_w + height
    print(("*") * width)