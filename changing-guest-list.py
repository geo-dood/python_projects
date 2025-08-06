# Author: George Maysack-Schlueter

# Initial list of dinner guests
dinner_guests = ['John', 'Jack', 'James', 'Jonas', 'Jim']

print("\nInitial Invitations:")
for guest in dinner_guests:
    print(f"Hello, {guest}! Would you like to come to a dinner party?")

# Handling a guest who can't attend
removed_guest = dinner_guests.pop(2)
print(f"\nUpdate: {removed_guest} will not be attending the dinner.")

# Replacing the unavailable guest
replacement_guest = 'Jamie'
dinner_guests.insert(2, replacement_guest)

print("\nRevised Invitations:")
for i, guest in enumerate(dinner_guests):
    name = guest.upper() if i == 2 else guest
    print(f"Hello, {name}! Would you like to come to a dinner party?")

print(f"\nNote: {replacement_guest} has taken {removed_guest}'s spot at the table.")
