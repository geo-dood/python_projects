# Author: George Maysack-Schlueter

dinner_guests = ['John', 'Jack', 'James', 'Jonas', 'Jim']

def invite_guests(guests: list[str], uppercase_indices: list[int] = []):
    """Print invitations, uppercasing guests at specified indices."""
    for i, guest in enumerate(guests):
        name = guest.upper() if i in uppercase_indices else guest
        print(f"Hello, {name}! Would you like to come to a dinner party?")

print("\nInitial Invitations:")
invite_guests(dinner_guests, uppercase_indices=[2])

print(f"\nOh no! {dinner_guests[2]} will not be attending!")

# Replace guest who can't come
removed_guest = dinner_guests.pop(2)
dinner_guests.insert(2, 'Jamie')

print("\nWe need 5 guests, so here is the new invitation:\n")
invite_guests(dinner_guests, uppercase_indices=[2])

print(f"\nLook at that! {dinner_guests[2]} took {removed_guest}'s spot right in the middle!")

print('\nBROADCAST: Attention everyone! I have found a larger table. '
      'We now need 8 guests.\nNew invitees will be listed below in all caps\n')

# Add new guests
dinner_guests.insert(0, 'Jim-bob')
dinner_guests.insert(3, 'Jake')
dinner_guests.append('Jason')

print("Final Invitations:")
# Uppercase new guests: indices 0, 3, and last (7)
uppercase_new_guests = [0, 3, len(dinner_guests) - 1]
invite_guests(dinner_guests, uppercase_indices=uppercase_new_guests)

print(f"\nTOTAL GUESTS: {len(dinner_guests)}")
