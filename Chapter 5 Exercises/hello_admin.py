#Created 10/28/2022
#Exercise 5-8- Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
#  If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
#  Otherwise, print a generic greeting, such as Hello Jaden, than you for logging in again.
usernames = ['admin', 'j03y', 'm1ke', 'kev1n', '@shley']
for username in usernames:
  if username == 'admin':
    print("Hello admin, would you like a status report?")
  else:
    print(f"Hello {username}, nice to see you again.")
