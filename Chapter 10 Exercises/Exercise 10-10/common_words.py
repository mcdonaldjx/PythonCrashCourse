#Created 12/5/2022
#Exercise 10-10- Common Words: Write a program that reads the files you found at Project Gutenberg and determines how many times the word 'the' appears in each text.
from pathlib import Path
books_list = ['frankenstein.txt', 'moby_dick.txt', 'tarzan.txt']
total = 0
for book in books_list:
  path = Path(book)
  line = path.read_text()
  word_count = line.lower().count('the ')
  print(f"{book} contains {word_count} instances of the word \'the\'")
  total += word_count
print(f"{total} instances total")
