#Created 11/1/2022
#Exercise 6-7- People: Start with the program for Exercise 8-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.
people = []
for index in range(0,3):
  if index == 0:
    person = {'name': 'jared','age': 29,'state': 'texas', 'favorite_color': 'blue', 'favorite_number': 21}
  elif index == 1:
    person = {'name': 'jamal', 'age': 36, 'state': 'texas', 'favorite_color': 'red', 'favorite_number': 8}
  else:
    person = {'name': 'kenni', 'age': 31, 'state': 'texas', 'favorite_color': 'red', 'favorite_number': 6}
  people.append(person)
  
print("People in the list:")
for person in people:
  print(f"{person['name'].title()}'s info:")
  for key,value in person.items():
    print(f"\t{key.title()}: {value}")
