#Created 10/25/2022 by Jared
# Exercise 3-9- Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7, use len() to print a message indicating the number of people you're inviting to dinner.
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
#Start of Exercise 3-9 code
print(f"\n{len(invites)} guests invited to the dinner in the end")
