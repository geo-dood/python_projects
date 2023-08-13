# Author: George Maysack-Schlueter
my_foods: list[str] = ["Steak", "Cheese", "Soup", "Fried Rice",
                       "Chicken", "Ramen"]
friend_foods: list[str] = my_foods[:]
for food in my_foods:
    print(f"George: {food} is one of my favorites!")
print()
for food in friend_foods[:3]:
    print(f"Friend: Wow, {food} is also one of my favorites!")
for food in friend_foods[3:]:
    print(f"Friend: However, {food} is not one of my favorites.")
del friend_foods[-3:]
print(f"\nGeorge: I am adding Ice Cream to my list."
      f"\nFriend: I am adding Mochi, Cheesecake"
      f" and Italian Ice to my list.")
my_foods.append("Ice Cream")
friend_foods.append("Mochi")
friend_foods.append("Cheesecake")
friend_foods.append("Italian Ice")
print("\nGeorge: Here is a list of my favorite foods:")
for food in my_foods:
    print(food)
print("\nFriend: Here is a list of my favorite foods:")
for food in friend_foods:
    print(food)
