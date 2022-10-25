#Created 10/25/2022 by Jared
# Exercise 3-1- Greetings: Start with the list you used in Exercise 3-1, but instad of just printing each person's name, print a message to them. The text of each message should be the same, but each message should be personalized with the person's name.
names = ["Friend A", "Friend B", "Friend C", "Friend D", "Friend E"]
for index in range(1,len(names)+1,1):
  print(f"Greetings {names[-index]}!")
