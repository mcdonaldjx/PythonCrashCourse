#Created 11/2/2022
#Exercise 6-10- Favorite Numbers 2: Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then print each person's name along with their favorite numbers.
favorite_numbers = {'jared': [1,21, 10], 'kenni': [6, 1, 14], 'jamal': [8, 6, 24], 'mari': [8, 20, 13], 'derrick': [1, 25]}
for person in favorite_numbers.keys():
  print(f"{person.title()}'s favorite numbers are: ")
  for number in favorite_numbers[person]:
    print(f"\t{number}")
