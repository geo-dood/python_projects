# Author: George Maysack-Schlueter
import random

alien_color = ['blue', 'green', 'red', 'gold', 'diamond']
alien_value = [5, 10, 50, 1000000, 5000000]
user_score = 0

curr_alien_color = random.choice(alien_color)
user_in = input("Press enter to shoot an alien!")

if user_in.lower() == 'secret':
    user_score = user_score + alien_value[-2]
    print(f"EHRMAHGERD! YOU GOT THE SECRET {alien_color[-2].upper()} ALIEN!!!"
          f"\nTHAT IS ULTRA, MEGA, RARE!!!"
          f"\nThat's worth {alien_value[-2]} points!"
          f"\nSCORE: {user_score}")
elif curr_alien_color == alien_color[0]:
    user_score = user_score + alien_value[0]
    print(f"You shot a {curr_alien_color} alien"
          f"\nThat's worth {alien_value[0]} points!"
          f"\nSCORE: {user_score}")
elif curr_alien_color == alien_color[1]:
    user_score = user_score + alien_value[1]
    print(f"You shot a {curr_alien_color} alien"
          f"\nThat's worth {alien_value[1]} points!"
          f"\nSCORE: {user_score}")
elif curr_alien_color == alien_color[2]:
    user_score = user_score + alien_value[2]
    print(f"You shot a {curr_alien_color} alien"
          f"\nThat's worth {alien_value[2]} points!"
          f"\nSCORE: {user_score}")

curr_alien_color = random.choice(alien_color)
user_in = input("\nPress enter to shoot an alien!")

if user_in.lower() == 'super secret':
    user_score = user_score + alien_value[-1]
    print(f"WOW!!! YOU GOT THE SUPER SECRET {alien_color[-1].upper()} ALIEN!!!"
          f"\nTHAT IS ULTRA, SUPER, MEGA, RARE AND EXTREMELY TOP SECRET!!!"
          f"\nThat's worth {alien_value[-1]} points!"
          f"\nSCORE: {user_score}")
elif curr_alien_color == alien_color[0]:
    user_score = user_score + alien_value[0]
    print(f"You shot a {curr_alien_color} alien"
          f"\nThat's worth {alien_value[0]} points!"
          f"\nSCORE: {user_score}")
elif curr_alien_color == alien_color[1]:
    user_score = user_score + alien_value[1]
    print(f"You shot a {curr_alien_color} alien"
          f"\nThat's worth {alien_value[1]} points!"
          f"\nSCORE: {user_score}")
elif curr_alien_color == alien_color[2]:
    user_score = user_score + alien_value[2]
    print(f"You shot a {curr_alien_color} alien"
          f"\nThat's worth {alien_value[2]} points!"
          f"\nSCORE: {user_score}")
