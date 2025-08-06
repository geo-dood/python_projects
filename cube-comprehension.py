# Author: George Maysack-Schlueter

# List of cubed numbers from 1 to 10
cubed_nums: list[int] = [number ** 3 for number in range(1, 11)]

# Print each cubed number
for cube in cubed_nums:
    print(cube)

# Display slices of the list
print(f"\nThe first three items: {cubed_nums[:3]}")
print(f"The middle three items: {cubed_nums[4:7]}")
print(f"The last three items: {cubed_nums[-3:]}")
