#Created 10/26/2022
#Exercise 4-12 - More Loops: All version of food.py in this section have avoided using for loops when printing, to save space. Choose a version of foods.py, and write two for loops to print each list of foods.
my_foods = ["pizza", "falafel","carrot cake", "cannoli"]
friend_foods = my_foods[:]
friend_foods[3] = "ice cream"
print("My foods:")
for mf in my_foods:
  print(f"\t{mf}")
print("Friend's foods:")
for ff in friend_foods:
  print(f"\t{ff}")
