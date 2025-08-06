# Author: George Maysack-Schlueter

print("Please enter your top 5 favorite fruits:")

fruits: list[str] = []

while len(fruits) < 5:
    fruit = input(f"Fruit {len(fruits) + 1}: ").strip().lower()
    fruits.append(fruit)

print()

if 'apple' in fruits:
    print("The list contains apple.")
else:
    print("The list does not contain apple.")

if 'dragonfruit' in fruits:
    print("The list contains dragonfruit.")
else:
    print("The list does not contain dragonfruit.")

print(f"\nYour fruit list: {fruits}")
