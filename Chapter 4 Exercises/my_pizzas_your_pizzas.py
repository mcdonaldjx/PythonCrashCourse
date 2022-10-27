#Created 10/26/2022
#Exercise 4-11 - My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then do the following:
#  Add a new pizza to the original list.
#  Add a different pizza to the list friend_pizzas.
#  Prove that you have two separate lists. Print the message My favorite pizzas are:, then use a for loop to print the first list. Print the message My friend's favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropiate list.
favorite_pizzas = ['pepperoni', 'cheese', 'apple dessert']
friend_pizzas = favorite_pizzas[:]
favorite_pizzas.append("extra cheesy")
friend_pizzas.append("meat lover's")
print(f"My favorite pizzas are: {favorite_pizzas}")
print(f"My friend's favorite pizzas are: {friend_pizzas}")
