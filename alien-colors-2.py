# Author: George Maysack-Schlueter
import random

alien_colors = ['blue', 'green', 'red', 'gold', 'diamond']
alien_values = {
    'blue': 5,
    'green': 10,
    'red': 50,
    'gold': 1_000_000,      # Secret alien
    'diamond': 5_000_000    # Super secret alien
}

user_score = 0

# Define special keyword triggers
secret_codes = {
    'secret': 'gold',
    'super secret': 'diamond'
}

def shoot_alien(round_num, user_score):
    alien = random.choice(alien_colors)
    print(f"\nRound {round_num}:")
    user_input = input("Press enter to shoot an alien! ")

    code = user_input.lower().strip()
    if code in secret_codes:
        secret_alien = secret_codes[code]
        points = alien_values[secret_alien]
        print(f"\n🎉 WOW!!! You discovered the SECRET {secret_alien.upper()} ALIEN!")
        print(f"That's worth {points:,} points!")
    elif alien in alien_values:
        points = alien_values[alien]
        print(f"\nYou shot a {alien} alien!")
        print(f"That's worth {points:,} points!")
    else:
        points = 0
        print(f"\nOops! Something went wrong. No points this round.")

    user_score += points
    print(f"SCORE: {user_score:,}")
    return user_score

# Two rounds of alien shooting
user_score = shoot_alien(1, user_score)
user_score = shoot_alien(2, user_score)
