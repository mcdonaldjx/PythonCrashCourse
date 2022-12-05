#Created 12/5/2022
#Exercise 10-8- Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block executes properly.
from pathlib import Path
dog_path = Path('dogs.txt')
try:
    dogs = dog_path.read_text()
    print(f"List of Dogs:\n{dogs}")
    print()
except FileNotFoundError as e:
  print(f"{e.filename} is missing!")
cat_path = Path('cats.txt')
try:
    cats = cat_path.read_text()
    print(f"List of Cats:\n{cats}")
except FileNotFoundError as e:
  print(f"{e.filename} is missing!")
