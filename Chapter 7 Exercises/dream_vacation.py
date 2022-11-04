#Created 11/3/2022 by Jared
#Exercise 7-10- Dream Vacation: Write a program that polls users about their dream vacation. Include a block of code that prints the results of the poll.
still_polling = True
dream_vacays = {}
while still_polling:
  name = input("What's your name? ")
  destination = input("Where would you like to go for your dream vacation? ")
  dream_vacays[name] = destination
  response = input("Is there anyone else that would like to add their dream vacation? (yes/no) ")
  if response.lower() == 'no':
    still_polling = False
print("Polling Results:")
for name, dest in dream_vacays.items():
  print(f"\t{name.title()} would like to go to {dest.title()}")
