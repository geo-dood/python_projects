# Author: George Maysack-Schlueter

# This week's buffet menu
menu_items = ("pasta", "beans", "rice", "chicken", "potatoes", "steak")

print("\n==============================")
print("🍽️  This Week's Buffet Menu:")
print("==============================")
for item in menu_items:
    print(f" - {item.capitalize()}")

# Update menu for next week
next_week_menu = ("pasta", "beans", "rice", "fish", "potatoes", "tofu")

print("\n==============================")
print("🥗  Next Week's Buffet Menu:")
print("==============================")
for item in next_week_menu:
    print(f" - {item.capitalize()}")

print("==============================\n")
