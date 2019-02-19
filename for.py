# for q in range(3, 6):
    # print(q)

#(start#, stop before#, interval)
for q in range(1, 10, 2):
    if q == 5:
        print("spam")
    else:
        print(q)

print("\nPrint odd numbers")
#print odd numbers
count = 0

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)