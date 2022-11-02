#Created 11/1/2022
#Exercise 6-1- Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
person = {'first_name': 'jared', 'age': 29, 'state': 'texas', 'favorite_animal':'penguin'}
for info in person:
  print(f"{info} is {person[info]}")
