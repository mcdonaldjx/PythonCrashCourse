#Created 12/02/2022
#Exercise 10-2- Learning C: You can use the replace() method to replace any word in a string with a different word. Here's a quick example showing how to replace 'dog' with 'cat' in a sentence:
#   >>> message = "I really like dogs."
#   >>> message.replace('dog', 'cat')
#   'I really like cats.'
#   Read in each line from the file you just created, learning_python.txt, and replace the word Python with the name of another language. Print each modified line to the screen.
from pathlib import Path
path = Path('learning_python.txt')
file_contents = path.read_text()
lines = file_contents.splitlines()
for line in lines:
    if 'Python' in line:
        line = line.replace('Python','Java')
        print(line)
