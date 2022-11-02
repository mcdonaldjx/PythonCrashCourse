#Created 11/1/2022
#Exercise 6-6- Polling: Using the code in favorite_languages.py
# Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.
favorite_languages = {
  'jen': 'python',
  'sarah' : 'c',
  'edward' : 'rust',
  'phil' : 'python'
  }
should_take_poll = ['edward', 'jared', 'jen', 'david', 'chris']
for stp in should_take_poll:
  if stp in favorite_languages.keys():
    print(f"Thank you for taking the poll {stp.title()}")
  else:
    print(f"We invite you to take the poll {stp.title()}")
