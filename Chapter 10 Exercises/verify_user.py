#Created 12/5/2022 by Jared
#Exercise 10-14- Verify User: Modify your program from Exercise 10-13 in case the current user is not the person who last used the program. Before printing a welcome back message in greet_user(), ask the user if this is the correct username. If it’s not, call get_new_username() to get the correct username.
from pathlib import Path
import json

def get_stored_info(path):
  """Get stored information if available."""
  if path.exists():
    contents = path.read_text()
    user_info = json.loads(contents)
    return user_info

def get_new_info():
  path = Path('user_dictionary.json')
  user_dict = {}
  user_dict['username'] = input("Please enter your username: ")
  user_dict['age'] = int(input("Please enter your age: "))
  user_dict['favorite color'] = input("Please enter your favorite color: ")
  contents = json.dumps(user_dict)
  path.write_text(contents)
  print("Saved!")

def greet_user(user_info):
  saved_name = user_info['username']
  answer = input(f"Is your username {saved_name.title()}? Enter Y or N: ")
  if answer.lower()[0] == 'y':
      print(user_info)
  else:
    get_new_info()

path = Path('user_dictionary.json')
if path.exists():
  user_info = get_stored_info(path)
  greet_user(user_info)
else:
  get_new_info()
