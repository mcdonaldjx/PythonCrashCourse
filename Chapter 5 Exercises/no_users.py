#Created 10/31/2022
#Exercise 5-9- No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
#  If the list is empty, print the message We need to find some users!
#  Remove all of the usernames from your list, and make sure the correct message is printed.
usernames = []
if not usernames:
  print("We need to find some users!")
else:
  for username in usernames:
    if username == 'admin':
      print("Hello admin, would you like a status report?")
    else:
      print(f"Hello {username}, nice to see you again.")
