# Author: George Maysack-Schlueter
dinner_guests = ['John', 'Jack', 'James', 'Jonas', 'Jim']
# initial invitations
print(f'\nHello, {dinner_guests[0]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[1]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[2].upper()}! Would you like to come to a'
      f' dinner party?')
print(f'Hello, {dinner_guests[3]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[4]}! Would you like to come to a dinner party?')
# someone can't come
print(f'\nOh no! {dinner_guests[2]} will not be attending!')
# popping removed guest, storing as variable for later print
removed_guests = dinner_guests.pop(2)
dinner_guests.insert(2, 'Jamie')
# round 2 invitations
print('We need 5 guests, so here is the new invitation:\n')
print(f'Hello, {dinner_guests[0]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[1]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[2].upper()}! Would you like to come to a'
      f' dinner party?')
print(f'Hello, {dinner_guests[3]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[4]}! Would you like to come to a dinner party?')
print(f"\nLook at that! {dinner_guests[2]} took {removed_guests}'s spot right"
      f" in the middle!")
# found larger table
print('\nBROADCAST: Attention everyone! I have found a larger table. '
      'We now need 8 guests.\nNew '
      'invitees will be listed below in all caps\n')
# new guests
dinner_guests.insert(0, 'Jim-bob')
dinner_guests.insert(3, 'Jake')
dinner_guests.append('Jason')
# final invitations
print(f'Hello, {dinner_guests[0].upper()}! Would you like to come to a'
      f' dinner party?')
print(f'Hello, {dinner_guests[1]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[2]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[3].upper()}! Would you like to come to a'
      f' dinner party?')
print(f'Hello, {dinner_guests[4]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[5]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[6]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[7].upper()}! Would you like to come to a'
      f' dinner party?\n')

print(f'TOTAL GUESTS: {len(dinner_guests)}')
