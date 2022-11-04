#Created 11/3/2022 by Jared
#Exercise 7-9- No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
sandwich_orders = ['turkey', 'pastrami','meatball', 'pastrami','roasted chicken', 'phillycheese steak', 'pastrami']
finished_sandwiches = []
print("The shop is out of pastrami, so there won't be any pastrami sandwiches made.")
while 'pastrami' in sandwich_orders:
  sandwich_orders.remove('pastrami')
for sandwich in sandwich_orders:
  print(f"I made your {sandwich} sandwich.")
  finished_sandwiches.append(sandwich)
print("Sandwiches made:")
for finished in finished_sandwiches:
  print(f"\t{finished} sandwich")
