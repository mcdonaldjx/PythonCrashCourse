#Created 10/2/2022
#Exercise 10-1- Learning Python: Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far. Start each line with the phrase In Python you can. . . . Save the file as learning_python.txt in the same directory as your exercises from this chapter. Write a program that reads the file and prints what you wrote two times: print the contents once by reading in the entire file, and once by storing the lines in a list and then looping over each line.
from pathlib import Path
path = Path('learning_python.txt')
file_contents = path.read_text()
print(f"Contents of the file in one line:\n{file_contents}")
lines_read = file_contents.splitlines()
print(f"Contents of the file in line by line:")
for line in lines_read:
    print(f"\t{line}")
