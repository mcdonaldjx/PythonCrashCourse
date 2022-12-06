#Created 12/5/2022 by Jared
#Exercise 10-10- Favorite Number: Write a program that prompts for the user’s favorite number. Use json.dumps() to store this number in a file. Write a separate program that reads in this value and prints the message “I know your favorite number! It’s _____.”
from pathlib import Path
import json

path = Path('favorite_number.json')
if path.exists():
  contents = path.read_text()
  saved_data = json.loads(contents)
  print(f"I remember your favorite number! It's {saved_data}!")
else:
  try:  
    fave_number = int(input("Plese enter your favorite number so I can remember it: "))
  except ValueError:
      print("That wasn't a number!")
  else:
    print(f"Ok, I'll remember {fave_number}!")
    save_data = json.dumps(fave_number)
    path.write_text(save_data)
