# Author: George Maysack-Schlueter
print("Please provide your top 5 favorite fruits: ")

fruits: list[str] = []
num = 0
while len(fruits) < 5:
    num = num + 1
    fruit = input(f"{num}. ")
    fruits.append(fruit.lower())

if 'bananas' in fruits:
    print("You really like bananas!")
if 'apples' in fruits:
    print("You really like apples!")
if 'grapes' in fruits:
    print("You really like grapes!")
if 'mangoes' in fruits:
    print("You really like mangoes!")
if 'oranges' in fruits:
    print("You really like oranges!")
