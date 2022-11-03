#Created 11/2/2022 by Jared
#Exercise 7-5- Movie Tickets: A movie theater charges different ticket prices depending on a person's age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
age = ""
while age != 'quit':
  age = input("Enter your age for your ticket price, or -1 to quit: ")
  if age.lower() == 'quit' or int(age) < 0:
    break
  else:  
    age = int(age)
    if age < 3:
      print("\tYou're less than 3 yo, so your ticket is free!")
    elif 3 <= age <= 12:
      print(f"\tYou're {age} yo, so your ticket is $10")
    else:
      print(f"\tYou're over 12 yo, so your ticket is $15")
