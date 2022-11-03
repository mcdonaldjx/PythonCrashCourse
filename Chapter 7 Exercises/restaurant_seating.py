#Created 11/2/2022 by Jared
#Exercise 7-2- Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they'll have to wait for a table. Otherwise, report that their table is ready.
group_size = input("How many poeple are in your dinner group? ")
group_size = int(group_size)
if group_size > 8:
  print("You'll have to wait for a table.")
else:
  print(f"There's a table ready for your party of {group_size}")
