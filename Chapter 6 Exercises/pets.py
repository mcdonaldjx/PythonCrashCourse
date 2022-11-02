#Created 11/1/2022
#Exercise 6-8- Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner's name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.
pets = [
  {'name': "brandy", 'species': 'dog','breed':'german shepherd', 'age': 15, 'location': 'houston'},
  {'name': "gigi", 'species': 'dog','breed':'yorkie mix', 'age': 4, 'location': 'conroe'},
  {'name': "leo", 'species': 'cat','breed':'sokoke', 'age': 3, 'location': 'dallas'}
]
for pet in pets:
  print(f"Pet:")
  for item in pet:
    print(f"\t{item.title()}: {pet[item]}")
