# Author: George Maysack-Schlueter
from typing import Any

cubed_nums: list[int | Any] = [number ** 2 for number in range(1, 11)]
for cube in cubed_nums:
    print(cube)
print(f"\nThe first three items:{cubed_nums[:3]}\nThe middle three items:'"
      f"{cubed_nums[4:7]}"
      f"\nThe last three items:{cubed_nums[-3:]}")
