# Author: George Maysack-Schlueter

wisco_lakes = [
    'hook lake', 'fish lake', 'cherokee lake', 'sweet lake',
    'rice lake', 'kegonsa ', 'lake', 'mendota lake', 'monona lake',
    'stewart lake', 'crystal lake', 'lost lake', 'columbus lake'
]

print(f"\nHere is the raw list:\n{wisco_lakes}")

# Title-case all lake names (fix capitalization)
for index, lake in enumerate(wisco_lakes):
    wisco_lakes[index] = lake.strip().title()  # Also strip spaces

print(f"\nHere is the list with correct capitalization:\n{wisco_lakes}\n")
print(f"Here is the third item from the list: {wisco_lakes[2]}.\n")
print(f"Here is the last item from the list: {wisco_lakes[-1]}.\n")

favorite_lake = (
    f"My favorite lake on the list is {wisco_lakes[6]}\n"
    f"However, I know it as Lake Mendota. We can fix this...."
)
print(favorite_lake)

# Fix the incorrect lake name at index 6
wisco_lakes[6] = 'Lake Mendota'

print(
    f"{wisco_lakes}\nThere we go. Much better!\n"
    f"My favorite lake on the list is {wisco_lakes[6]}.\n"
)

print(
    f"Here is the list again:\n{wisco_lakes}\n"
    f"Number of Lakes in list = {len(wisco_lakes)}\n"
    f"However, I think it could use one more.\n"
)

wisco_lakes.append('Lake Hungry')

print(
    f"Here is the list, plus one:\n{wisco_lakes}\n"
    f"Number of Lakes in list = {len(wisco_lakes)}\n"
    f"I still think it could use one more. Not at the end though. "
    f"Let us put it in the middle.\n"
)

wisco_lakes.insert(7, 'Lake Ripley')

print(
    f"Here is the updated list, with a new entry after Lake Mendota:\n"
    f"{wisco_lakes}\nNumber of Lakes in list = {len(wisco_lakes)}\n"
    f"You know what, I changed my mind. I am going to remove some now.\n"
)

# Remove four entries
wisco_lakes.remove('Fish Lake')
del wisco_lakes[9]
wisco_lakes.pop()
wisco_lakes.pop(5)

print(
    f"Here is the new list, with 4 entries removed:\n{wisco_lakes}\n"
    f"Number of Lakes in list = {len(wisco_lakes)}\n"
    f"That looks good. However, things are all unsorted now... "
    f"Let us fix that.\n"
)

wisco_lakes.sort()

print(
    f"Here is our new sorted list:\n{wisco_lakes}\n"
    f"I think I prefer reverse alphabetical order...\n"
)

wisco_lakes.sort(reverse=True)

print(
    f"Here is our reverse sorted list:\n{wisco_lakes}\n"
    f"I cannot make up my mind. Let us temporarily switch to alphabetical order again."
)

print(sorted(wisco_lakes))

print(
    f"\nAnd reverse once more:\n{wisco_lakes}\n"
    f"I like alphabetical best - let us switch back to it permanently.\n"
)

wisco_lakes.reverse()

print(
    f"Here is our list, back to alphabetical order:\n{wisco_lakes}\n"
    f"Final Number of Lakes in list = {len(wisco_lakes)}"
)
