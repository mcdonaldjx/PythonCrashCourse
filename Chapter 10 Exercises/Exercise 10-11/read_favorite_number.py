#Created 12/5/2022 by Jared
#Exercise 10-10- Favorite Number: Write a  program that reads in a stored number in a file and prints the message “I know your favorite number! It’s _____.”
from pathlib import Path
import json

path = Path('favorite_number.json')
if path.exists():
  contents = path.read_text()
  saved_data = json.loads(contents)
  print(f"I remember your favorite number! It's {saved_data}!")
else:
  print("I don't remember your favorite number!")
