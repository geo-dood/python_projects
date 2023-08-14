# Author: George D. Maysack-Schlueter
numbers = range(1, 10)

for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    elif number in range(4, 10):
        print(f'{number}th')
