# Author: George D. Maysack-Schlueter

# Define possible alien colors and initialize score
alien_colors = ['green', 'yellow', 'red']
score = 0

def shoot_alien(current_color, next_color, score, points_awarded):
    """
    Handles one round of user interaction with an alien:
    - Prompts user to shoot
    - Updates score based on action
    - Displays result
    """
    print(f"\nA {current_color} alien has appeared.")
    print(f"Your score is: {score}")
    user_input = input("Enter 'x' to shoot the alien! --> ")

    if user_input.lower() == 'x':
        score += points_awarded
        print(f"\nYou shot the alien!\nThe alien has turned {next_color}!"
              f"\n\nYou have earned {points_awarded} points!\nYour score is: {score}")
    else:
        print(f"\nYou did not shoot the alien."
              f"\nThe alien is still {current_color}"
              f"\n\nYou earned 0 points\nYour score is: {score}")

    return score

# Round 1
score = shoot_alien(alien_colors[0], alien_colors[1], score, 5)

# Round 2
score = shoot_alien(alien_colors[1], alien_colors[2], score, 10)
