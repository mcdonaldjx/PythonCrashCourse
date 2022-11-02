#Created 11/1/2022
#Exercise 6-2- Favorite Numbers: Use a dictionary to store people's favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person's name and favorite number.
favorite_numbers = {'jared': 21, 'kenni': 6, 'jamal': 8, 'mari': 8, 'derrick': 1}
for fn in favorite_numbers:
  print(f"{fn.title()}'s favorite number is {favorite_numbers[fn]}")
