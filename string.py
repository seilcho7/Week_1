name = "Milla Cookie Pants Jovovich"

# stop = 10
counter = 0

while counter < len(name):
    if (counter % 2 == 0) and name[counter] != " ":
        print(name[counter], counter)
    counter = counter + 1