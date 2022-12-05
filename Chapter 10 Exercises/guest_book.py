#Created 12/4/2022
#Exercise 10-5- Guest Book: Write a while loop that prompts users for their name. Collect all the names that are entered, and then write these names to a file called guest_book.txt. Make sure each entry appears on a new line in the file.
from pathlib import Path
file_path = Path('guest_book.txt')
names_list = ""
while True:
  name = input("Please enter a name for the guest book or \'exit\' to quit: ")
  if name.lower() == 'exit':
    break;
  else:
    names_list += name+"\n"
file_path.write_text(names_list)
