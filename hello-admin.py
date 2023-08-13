# Author: George Maysack-Schlueter
current_users = ['alice0', 'bob1', 'carol2', 'david3', 'edward4', 'admin']

user_in = input("\nPlease provide a username --> ")

if user_in:
    if user_in.lower() == "admin":
        print(f"Hello {user_in.lower()} - Would you like a status report?")
    elif user_in.lower() in current_users:
        print(f"Hello {user_in.lower()}!")
    else:
        print(f"\nUser {user_in} not found...")
        user_input = input("\nCreate new user? (Y/N) --> ")
        if user_input.lower() == "y":
            new_username = input("\nEnter new username --> ")
            if new_username.lower() not in current_users:
                print(f"\nUsername {new_username} Available! "
                      f"User registered successfully.")
                current_users.insert(-1, new_username.lower())
            elif new_username.lower() in current_users:
                print(f"\nUsername {new_username} already exists!")
                new_username = input("\nPlease try again --> ")
                if new_username.lower() not in current_users:
                    current_users.insert(-1, new_username.lower())
                    print(f"\nUsername {new_username} Available! "
                          f"User registered successfully.")
                elif new_username.lower() in current_users:
                    print(f"\nUsername {new_username} already exists! "
                          f"Please try a different username. Exiting...")
else:
    print("\nPlease provide a username...")

print(f'\n{current_users}')
