# Author: George Maysack-Schlueter
dinner_guests = ['John', 'Jack', 'James', 'Jonas', 'Jim']
# initial invitations
print(f'\nHello, {dinner_guests[0]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[1]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[2].upper()}! Would you like to come to '
      f'a dinner party?')
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
print(f'Hello, {dinner_guests[2].upper()}! Would you like to come to '
      f'a dinner party?')
print(f'Hello, {dinner_guests[3]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[4]}! Would you like to come to a dinner party?')
print(f"\nLook at that! {dinner_guests[2]} took {removed_guests}'s "
      f"spot right in the middle!")
# found larger table
print('\nBROADCAST: Attention everyone! I have found a larger table. '
      'We now need 8 guests.\nNew invitees will be '
      'listed below in all caps\n')
# new guests
dinner_guests.insert(0, 'Jim-bob')
dinner_guests.insert(3, 'Jake')
dinner_guests.append('Jason')
# 3rd round invitations
print(f'Hello, {dinner_guests[0].upper()}! Would you like to come to '
      f'a dinner party?')
print(f'Hello, {dinner_guests[1]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[2]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[3].upper()}! Would you like to come to '
      f'a dinner party?')
print(f'Hello, {dinner_guests[4]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[5]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[6]}! Would you like to come to a dinner party?')
print(f'Hello, {dinner_guests[7].upper()}! Would you like to come to '
      f'a dinner party?')
# table is not coming
print('\nUnfortunately my new table will not arrive in time'
      '\nEven more unfortunately, I have already sold my other '
      'table\nI only have room for 2 guests now!\n')
# uninviting 6 guests
print(f'Sorry, {dinner_guests.pop()}, you have been uninvited '
      f'from my awesome party')
print(f'Sorry, {dinner_guests.pop()}, you have been uninvited '
      f'from my awesome party')
print(f'Sorry, {dinner_guests.pop()}, you have been uninvited '
      f'from my awesome party')
print(f'Sorry, {dinner_guests.pop()}, you have been uninvited '
      f'from my awesome party')
print(f'Sorry, {dinner_guests.pop()}, you have been uninvited '
      f'from my awesome party')
print(f'Sorry, {dinner_guests.pop()}, you have been popped off the guest list.')
# informing last 2 guests they are still invited
print(f'\nCongratulations, {dinner_guests[0]}, you are still '
      f'invited to my awesome party!')
print(f'Congratulations, {dinner_guests[1]}, you are still '
      f'invited to my awesome party!\n')
# emptying list
del dinner_guests[0]
del dinner_guests[0]
print(dinner_guests)
