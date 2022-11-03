#Created 11/2/2022
#Exercise 7-3- Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not
number = input("Enter a number to check if it is a multiple of 10: ")
number = int(number)
if number % 10 == 0:
  print(f"{number} is a multiple of 10!")
else:
  print(f"{number} is NOT a multiple of 10!")
