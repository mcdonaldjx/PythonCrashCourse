#Created 10/25/2022 by Jared
# Exercise 3-6- More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#  Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
#  Use insert() to add one new guest to the beginning of your list.
#  Use insert() to add one new guest to the middle of your list.
#  Use append() to add one new guest to the end of your list.
#  Print a new set of invitation messages, one for each person in your list.
invites = []
invites.append("Andre Benjamin")
invites.append("Barack Obama")
invites.append("Denzel Washington")
invites.append("Jamie Foxx")
for i in invites:
  print(f"Join me for dinner please, {i}")
print(f"\n{invites[0]} can't make it to the dinner.\n")
invites[0] = "Kendrick Lamar"
for i in range(0, len(invites)):
  print(f"Please join me for dinner {invites[i]}")

print("\nI've found a bigger table, so more guests are invited\n")
invites.insert(0, "Derrick Rose")
invites.insert(int(len(invites)/2), "Dr. Julius Erving")
invites.append("Vince Carter")
for index in range(0, len(invites)):
  print(f"Please join me for dinner {invites[index]}.")
