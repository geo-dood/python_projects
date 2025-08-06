# Author: George Maysack-Schlueter

# Generate and print cubes of numbers from 1 to 10
cubed_nums: list[int] = [number ** 3 for number in range(1, 11)]

for cube in cubed_nums:
    print(cube)
