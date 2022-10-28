#Created 10/27/2022
#Exercise 4-13- Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
# Use a for loop to print each food the restaurant offers.
# Try to modify one of the items, and make sure that Python rejects the change.
# The restauraunt changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
foods = ("corn", "chicken","potatoes", "steak", "rice")
print("Foods the restaurant offer:")
for food in foods:
    print(f"\t{food}")
#foods[0] = "corn on the cob" #Trying to change one element of the tuple
print("The restaurant changed its menu to:")
foods = ("corn", "baked chicken","potatoes", "steak", "dirty rice")
for food in foods:
  print(f"\t{food}")
