#Created 10/24/2022
#Chapter 2, Exercise 8- File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
filename = 'python_notes.txt'
filename_no_suffix = filename.removesuffix('.txt')
print(f"File name = {filename}\nFile name after removing the suffix:{filename_no_suffix}")
