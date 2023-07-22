user_name = input("\nWhat is your name?\n")
space_name = f'\t\t{user_name.title()}\t\t'
print("\n------------------------------------------------\n")
print(f'Unstripped:\n***{space_name}***\n')
print(f'Left Strip:\n***{space_name.lstrip()}***\n\nRight Strip:\n***{space_name.rstrip()}***\n\nDouble Strip:\n***{space_name.strip()}***')
