#Created 10/24/2022
#Chapter 2, Exercise 7- Stripping Names: Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
name = input("What is your name?")
name = f"\n\t{name}\n\t"
print(f"Your name had whitespace in it. Here's the input: [{name}]\nYour name after removing whitespace to the left: [{name.lstrip()}]\nYour name after removing whitespace to the right: [{name.rstrip()}]\nYour name after removing all whitespace: [{name.strip()}]")
