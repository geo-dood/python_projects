# Author: George Maysack-Schlueter
alien_colors = ['green', 'yellow', 'red']

start_score = 0
current_alien_color = alien_colors[0]

print(f"\nA {current_alien_color} alien has appeared."
      f"\nYour score is: {start_score}")
user_in = input("Enter 'x' to shoot the alien! --> ")

if user_in.lower() == 'x':
    current_alien_color = alien_colors[1]
    current_score = start_score + 5
    print(f"\nYou shot the alien!\nThe alien has turned {current_alien_color}!"
          f"\n\nYou have earned 5 points!\nYour score is: {current_score}")
else:
    print(f"\nYou did not shoot the alien."
          f"\nThe alien is still {current_alien_color}"
          f"\n\nYou earned 0 points\nYour score is: {start_score}")

user_in = input("\nEnter 'x' to shoot the alien! --> ")
if user_in.lower() == 'x':
    current_alien_color = alien_colors[2]
    current_score = start_score + 10
    print(f"\nYou shot the alien!\nThe alien has turned {current_alien_color}!"
          f"\n\nYou have earned 5 points!\nYour score is: {current_score}")
else:
    print(f"\nYou did not shoot the alien. Twice..."
          f"\nThe alien is still {current_alien_color}"
          f"\n\nYou earned 0 points\nYour score is: {start_score}")
