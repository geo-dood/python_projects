# Author: George Maysack Schlueter
fav_nums = {'alice' : 16,
            'bob'   : 53,
            'carl'  : 1,
            'dan'   : 23,
            'eddy'  : 7,
            'frank' : 3,
            'george': 13,
            'henry' : 444
            }

for person in fav_nums:
    print(f"{person.title()}'s favorite number is {fav_nums[person]}!")
