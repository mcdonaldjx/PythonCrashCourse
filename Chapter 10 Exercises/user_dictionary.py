#Created 12/5/2022 by Jared
#Exercise 10-13- User Dictionary: Write a program that asks for three pieces of information about the user, then store all the information you collect in a dictionary. Write this dictionary to a file using json.dumps(), and read it back in using json.loads(). Print a summary showing exactly what your program remembers about the user.
from pathlib import Path
import json

def get_stored_info(path):
  """Get stored information if available."""
  if path.exists():
    user_info = path.read_text()
    return user_info

def get_new_info():
  path = Path('user_dictionary.json')
  user_dict = {}
  user_dict['name'] = input("Please enter your name: ")
  user_dict['age'] = int(input("Please enter your age: "))
  user_dict['favorite color'] = input("Please enter your favorite color: ")
  contents = json.dumps(user_dict)
  path.write_text(contents)

def greet_user(user_info):
  print("Here's the information that was stored:")
  print(user_info)

path = Path('user_dictionary.json')
if path.exists():
  user_info = get_stored_info(path)
  greet_user(user_info)
else:
  get_new_info()
