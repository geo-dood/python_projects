# Author: George D. Maysack-Schlueter
name = input('Please enter your name: ')
age_in = input('Please enter your age: ')
age = int(age_in)
birth_month = input('Please enter birth month: ')
fav_food = input('Please enter favorite food: ')
fav_color = input('Please enter favorite color: ')
fav_szn = input('Please enter your favorite season: ')

if name.lower() != 'george':
    print('Your name is not George.')
else:
    print('Wow, your name is George?!')

print(f'Checking if your name is Sally --> {name == "Sally"}')

if age < 21:
    print('Would you like some sparkling water?')
else:
    print('Would you like a beer?')

if birth_month.lower() == 'september':
    print('September is the best month of all!')
else:
    print(f'Your birth month is {birth_month.title()}. Cool!')

if fav_szn.lower() == "spring":
    print('Spring huh? I love watching everything bloom as well!')
if fav_szn.lower() == "summer":
    print('Summer, huh? I love those long, hot days too!')
if fav_szn.lower() == "fall":
    print('The Fall is my favorite too. Does not get better than those leaves!')
if fav_szn.lower() == "winter":
    print('Winter...Burr! So pretty, but so bone chilling!')

if fav_color.lower() == 'green':
    print('Wow! Green is also my favorite color.')
else:
    print(f'Nice! {fav_color.title()} is a gorgeous color!')

if fav_food.lower() == 'steak':
    print('Wow! Steak is also my favorite food. We have that in common!')
else:
    print(f'I have never had {fav_food.lower()} before. Bring me some!')
