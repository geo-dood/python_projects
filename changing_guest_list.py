# Author: George Maysack-Schlueter
dinner_guests = ['John', 'Jack', 'James', 'Jonas', 'Jim']
# initial invitations
for person in dinner_guests:
    print(f"Hello,{person}! Would you like to come to a dinner party?")

# someone can't come
print(f'\nOh no! {dinner_guests[2]} will not be attending!')
# popping removed guest, storing as variable for later print
removed_guests = dinner_guests.pop(2)
dinner_guests.insert(2, 'Jamie')
print('We need 5 guests, so here is the new invitation:\n')
print(f'Hello, {dinner_guests[0]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[1]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[2].upper()}! Would you like to come to a '
      f'dinner party?')
print(f'Hello, {dinner_guests[3]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[4]}! Would you like to come to a dinner party?')
print(f"\nLook at that! {dinner_guests[2]} took {removed_guests}'s"
      f" spot right in the middle!")
