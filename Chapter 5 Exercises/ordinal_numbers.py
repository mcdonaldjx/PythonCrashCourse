#Created 10/31/2022
#Exercise 5-11- Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
#  Store the numbers 1 through 9 in a list
#  Loop through the list.
#  Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number, one per line.
numbers = list(range(1,10))
for num in numbers:
  if num == 1:
    print("1st")
  elif num == 2:
    print("2nd")
  elif num == 3:
    print("3rd")
  else:
    print(f"{num}th")
