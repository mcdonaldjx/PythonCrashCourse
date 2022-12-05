#Created 12/5/2022
#Exercise 10-6- Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers. Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.
try:
  a = int(input("Please enter a number to add: "))
except ValueError:
  print("That is not a number.")
else:
  try:
      b = int(input(f"Please enter a number to add to {a}: "))
  except ValueError:
    print("That is not a number.")
  else:
    print(f"{a}+{b} = {(a+b)}")
