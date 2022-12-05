#Created 12/5/2022
#Exercise 10-7- Addition Calculator: Wrap your code from Exercise 10-5 in a while loop so the user can continue entering numbers, even if they make a mistake and enter text instead of a number.
while True:
  try:
    a = input("Please enter a number to add or \'quit\' to exit: ")
    if a == 'quit':
      break
    else:
      a = int(a)
  except ValueError:
    print("That is not a number.")
  else:
    try:
      b = input(f"Please enter a number to add to {a} or \'quit\' to exit: ")
      if b == 'quit':
        break
      else:
        b = int(b)
    except ValueError:
      print("That is not a number.")
    else:
      print(f"{a}+{b} = {(a+b)}")
