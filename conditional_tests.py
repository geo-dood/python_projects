# Author: George Maysack-Schlueter
print("Please provide your top 5 favorite fruits: ")

fruits: list[str] = []

while len(fruits) < 5:
    fruit = input()
    fruits.append(fruit.lower())

if 'apple' in fruits:
    print("The list contains apples!")
else:
    print('The list does not contain apples!')

if 'dragonfruit' in fruits:
    print("The list contains dragonfruit!")
else:
    print('The list does not contain dragonfruit!')

print(fruits)
