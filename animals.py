# Author: George Maysack-Schlueter

import random

# List of black-and-white animals
bnw_animals = ['panda', 'zebra', 'dalmatian', 'skunk', 'penguin']

# Divide by coat vs feathers
coat_animals = bnw_animals[:-1]
feathered_animal = bnw_animals[-1]

print()  # Initial spacing

# Describe each animal
for animal in coat_animals:
    print(f"The {animal} has a black and white coat—very striking.")

# Special case for the penguin
print(f"\nAnd the {feathered_animal}? Black and white feathers. Incredible!")

# Fun fact
random_animal = random.choice(bnw_animals)
print(f"\nFun fact: Did you know the {random_animal} is black and white for camouflage?")
