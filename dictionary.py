# meal = {
#     "drink": "Creatures Comforts Athena",
#     "appetizer": "Charcuterie",
#     "dinner": "Grindhouses burger",
#     "dessert": "Cupcakes"
# }

# house = {
#     'kitchen': 'Fancy Refrigerator',
#     'bathrooms': 3,
#     'bedrooms': 4,
#     'living_room': 'giant'
# }

# user = {
#     'first_name': 'Sean',
#     'last_name': 'Reid'
# }

# print(meal['dessert'])
# print(house['bathrooms'])
# print(user['first_name'])

# print('%s would like %s from the %s' % (user['first_name'], house['kitchen'], meal['dessert']))

# if 'cigar' in meal:
#     print('Cuba, we have a cigar.')
# else:
#     print('No cigars')

# if 'last_name' in user:
#     print('You have last name')
# else:
#     print('No last name')

# meal['water'] = 'Tap'
# meal['bread'] = True
# meal['drink'] = 'Water'

# print(meal)

# del meal['water']

# print(meal)

digitalcrafts = {
    'US': {
        'Georgia': {
            'Atlanta': '3423 Piedmont RD NE $420',
        },
        'Texas': {
            'Houston': '3302 Canel ST.'
        }
    }
}

# print(digitalcrafts['US']['Georgia']['Atlanta'])

# digitalcrafts['US']['Florida'] = {}
# digitalcrafts['US']['Washington'] = {'Seattle': '123 Pearl Jam Ave'}
# digitalcrafts['Canada'] = {'British Columbia': {'Vancouver': '454 Canuck ST.'}}

# # print(digitalcrafts)

# countries = digitalcrafts.keys()
# us_states = digitalcrafts['US'].keys()

# def us_cities(states):
#     cities =[]
#     for key in states:
#         print('there are campuses in %s' % (key))

# us_cities(us_states)

for country in digitalcrafts:
    for state in digitalcrafts[country]:
        print(country, state, end = ': ')
        for city in digitalcrafts[country][state]:
            print(city)