#Created 12/5/2022 by Jared
#Exercise 10-11- Favorite Number: Write a program that prompts for the user’s favorite number. Use json.dumps() to store this number in a file.
from pathlib import Path
import json
path = Path('favorite_number.json')
try:    
  fave_number = int(input("Plese enter your favorite number so I can remember it: "))
except ValueError:
  print("That wasn't a number!")
else:
  print(f"Ok, I'll remember {fave_number}!")
  save_data = json.dumps(fave_number)
  path.write_text(save_data)
