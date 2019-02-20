# Display a menu asking whether to check in or check out.
# Prompt the user for a floor number, then a room number.
# If checking in, ask for the number of occupants and what their names are.
# If checking out, remove the occupants from that room.
# Do not allow anyone to check into a room that is already occupied.
# Do not allow checking out of a room that isn't occupied.

hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}

check = input('Check in or check out?: ')
floor_number = input('Floor number?: ')
room_number = input('Room number?: ')
occupant_counter = 0
name_list = []

# ask number of occupants and their names
if check == 'in':
    occupant_number = input('How many occupants?: ')
    while int(occupant_number) > occupant_counter:
        ask_name = input('Name: ')
        name_list.append(ask_name)
        occupant_counter += 1
    
    # check and see if floor number and room is available, and then add new occupants
    for floor in hotel:
        if floor_number in floor:
            if room_number not in hotel[floor]:
                hotel[floor][room_number] = name_list
                break
            else:
                print("Room is already occupied.")
                break
        else:
            hotel[floor_number][room_number] = name_list
            break
        break

# check out occupants if floor number and room number is correct
elif check == 'out':
    for floor in hotel:
        if floor in floor_number:
            if room_number in hotel[floor]:
                del hotel[floor][room_number]
            else:
                print("Room number is not correct.")
        else:
            print("Please check the floor number again.")

print(hotel)