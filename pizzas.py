# Author: George Maysack-Schlueter
fav_pizzas = ['pepperoni', 'cheese', 'sausage']
friend_pizzas = fav_pizzas[:]
print("Here is a list of my favorite pizzas:")
for pizza in fav_pizzas:
    print(f'{pizza.title()} pizza')
print('As you can tell, I really love pizza.\n')
print("Here is a list of my Friends favorite pizzas:")
for pizza in friend_pizzas:
    print(f'{pizza.title()} pizza')
print('As you can tell, my Friend really loves pizza.'
      '\n\nWe can each add one more '
      f'to keep our lists unique...\n')
fav_pizzas.append("Bacon")
friend_pizzas.append("Pineapple")
print("Here is an updated list of my favorite pizzas:")
for pizza in fav_pizzas:
    print(f'{pizza.title()} pizza')
print("\nHere is an updated list of my Friends favorite pizzas:")
for pizza in friend_pizzas:
    print(f'{pizza.title()} pizza')
