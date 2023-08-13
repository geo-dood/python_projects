# Author: George Maysack-Schlueter
vacation_spots = ['kyoto', 'venis', 'london', 'athens', 'rome', 'paris',
                  'tokyo', 'barcelona', 'new york', 'sydney']
print(f'\nUnsorted Locations------------------(B): {vacation_spots}')
print(f'\nSorted Function Alpha Order---------(T): {sorted(vacation_spots)}')
print(f'\nUnsorted Locations------------------(B): {vacation_spots}')
print(f'\nFunction  Reverse-------------------(T): '
      f'{sorted(vacation_spots, reverse=True)}')
print(f'\nUnsorted Locations------------------(B): {vacation_spots}')
vacation_spots.reverse()
print(f'\nMethod Reverse----------------------(P): {vacation_spots}')
vacation_spots.reverse()
print(f'\nReversed Reverse Method-------------(P): {vacation_spots}')
vacation_spots.sort()
print(f'\nSort Method Alpha Order-------------(P): {vacation_spots}')
vacation_spots.sort(reverse=True)
print(f'\nSort Method Reverse Alpha Order-----(P): {vacation_spots}')
