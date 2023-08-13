# Author: George Maysack-Schlueter
from typing import Any

cubed_nums: list[int | Any] = [number ** 3 for number in range(1, 11)]
for cube in cubed_nums:
    print(cube)
