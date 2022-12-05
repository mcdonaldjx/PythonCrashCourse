#Created 12/4/2022
#Exercise 10-4- Guest: Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.
from pathlib import Path
name = input("Please enter your name to write it to a file: ")
path = Path('guest.txt')
path.write_text(name)
