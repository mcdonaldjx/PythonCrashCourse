#Created 10/25/2022 by Jared
# Exercise 3-5 - Changing Guest List: You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite.
#  Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can't make it.
#  Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting.
#  Print a second set of invitation messages, one for each person who is still in your list.
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
  
