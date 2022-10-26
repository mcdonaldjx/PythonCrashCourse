#Created 10/25/2022 by Jared
# Exercise 3-7- Shrinking Guest List: You just found out that your new dinner table won't arrive in time for the dinner, and now you have space for only two guests.
#  Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#  Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you're sorry you cant invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they're still invited.
#  Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
invites = []
invites.append("Andre Benjamin")
invites.append("Barack Obama")
invites.append("Denzel Washington")
invites.append("Jamie Foxx")
for i in invites:
  print(f"Join me for dinner please, {i}")
#Start of Exercise 3-5 code
print(f"\n{invites[0]} can't make it to the dinner.\n")
invites[0] = "Kendrick Lamar"
for i in range(0, len(invites)):
  print(f"Please join me for dinner {invites[i]}")
#Start of Exerise 3-6 code
print("\nI've found a bigger table, so more guests are invited\n")
invites.insert(0, "Derrick Rose")
invites.insert(int(len(invites)/2), "Dr. Julius Erving")
invites.append("Vince Carter")
for index in range(0, len(invites)):
  print(f"Please join me for dinner {invites[index]}.")
#Start of Exercise 3-7 code
print("\nSorry, but I can only invite two people to dinner!\n")
while len(invites) > 2:
  uninvited_guest = invites.pop()
  print(f"Sorry {uninvited_guest}, but I can only invite two people to dinner.")
for i in range(0, len(invites)):
  print(f"{invites[i]}, you're still invited to the dinner.")
del invites[-1]
del invites[0]
