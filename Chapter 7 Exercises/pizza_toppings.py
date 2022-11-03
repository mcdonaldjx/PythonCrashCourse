#Created 11/2/2022 by Jared
#Exercise 7-4- Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you'll add that topping to their pizza.
topping = ""
while topping.lower() != 'quit':
  topping = input("Please enter a topping to add to your pizza: ")
  if topping.lower() == 'quit':
    break
  else:
    print(f"We'll add {topping} to your pizza.")
