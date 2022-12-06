#Created 12/5/2022 by Jared
#Exercise 10-12- Favorite Number Remembered: Combine the two programs you wrote in Exercise 10-11 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user’s favorite number and store it in a file. Run the program twice to see that it works.
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
