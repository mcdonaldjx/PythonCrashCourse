#Created 10/25/2022 by Jared
# Exercise 3-1- Names: Store the names of a few of your friends in a list called names. Print each person's name by accessing each element in the list, one at a time.#
names = ["Friend A", "Friend B", "Friend C", "Friend D", "Friend E"]
for index in range(len(names),0, -1):
  print(names[-index])
