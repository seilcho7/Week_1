user_input = input('Please enter a word: ')

lists = {}

for i in user_input:
    if i in lists:
        lists[i] += 1
    elif i not in lists:
        lists[i] = 1

print(lists)
