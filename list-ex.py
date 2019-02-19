## sum the numbers
# numbs = [-2, -1, 0, 1, 2, 3, 4]
# factor = 2
# print(sum(numbs))

# #largest number
# print(max(numbs))

## smallest number
# print(min(numbs))

## even numbers
# index = 0
# while index < len(numbs):
#     if numbs[index] % 2 == 0:
#         print(numbs[index])
#     index += 1

## positive numbers 1, 2
# index_two = 0
# pos_numbs = []
# while index_two < len(numbs):
#     if numbs[index_two] > 0:
#         print(numbs[index_two])
#         pos_numbs.append(numbs[index_two])
#     index_two += 1
# print(pos_numbs)


## multiply a list
# new_list = []
# while index < len(numbs):
#     new_list.append(numbs[index] * factor)
#     index += 1
# print(new_list)


## multiply vectors
# num_one = [2, 4, 5]
# num_two = [2, 3, 6]
# new_num = []
# while index < len(num_one):
#     new_num.append(num_one[index] * num_two[index])
#     index += 1
# print(new_num)

## matrix addition
# matrix_one = [[1, 3], [2, 4], [1, 2]]
# matrix_two = [[5, 2], [1, 0], [8, 6]]
# matrix_three = []
# index = 0
# counter = 0
# while index < len(matrix_one):
#     while counter < len(matrix_one[1]):
#         if counter == 0:
#             matrix_three.append([0, 0])
#         matrix_three[index][counter] = (matrix_one[index][counter] + matrix_two[index][counter])
#         counter += 1

#     index += 1
#     counter = 0

# print(matrix_three[0:len(matrix_one)])
# print(matrix_three)

## de-dup
li_one = ["a", "b", "c", "d", 1, 7]
li_two = ["a", "a", "b", "d", 1]
added = []
remove_dup = []

added = li_one + li_two

def add_new(list):
    for x in list:
        if x not in remove_dup:
            remove_dup.append(x)
    print(remove_dup)

add_new(added)