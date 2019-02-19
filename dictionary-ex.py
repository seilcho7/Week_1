# # exercise 1
# phonebook_dict = {
#     'Alice': '703-493-1834',
#     'Bob': '857-384-1234',
#     'Elizabeth': '484-584-2923'
# }

# # 1: print elizabeth's phone number
# print(phonebook_dict['Elizabeth'])

# # 2: add an entry to the dictionary: Kareem's number is 938-489-1234
# phonebook_dict['Kareem'] = '938-489-1234'

# # 3: delete alice's phone entry
# # phonebook_dict['Alice'] = ''
# # phonebook_dict.pop('Alice')
# del phonebook_dict['Alice']

# # 4: change bob's phone number to '968-345-2345'
# phonebook_dict['Bob'] = '968-345-2345'

# # 5: print all the phone entries
# print(phonebook_dict)

# exercise 2
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# 1: write a python expression that gets the email address of Ramit
print(ramit['email'])

# 2: write a python expression that gets the first of ramit's interest
print(ramit['interests'][0])

# 3: write a python expression that gets the email address of jasmine
print(ramit['friends'][0]['email'])

# 4: write a python expression that gets the second of jan's two interests
print(ramit['friends'][1]['interests'][1])