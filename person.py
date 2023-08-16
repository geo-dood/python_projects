# Author: George D. Maysack Schlueter
bob_dict = dict(name='bob', age=42,
                occupation='builder',
                fav_thing='construction')

print(f"{bob_dict['name'].title()} is a {bob_dict['occupation']}."
      f"\n{bob_dict['name'].title()} is {bob_dict['age']} years old."
      f"\n{bob_dict['name'].title()}'s favorite thing "
      f"is {bob_dict['fav_thing']}!")
