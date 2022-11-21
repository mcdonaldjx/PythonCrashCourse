#Created 11/21/2022 by Jared
#Exercise 8-4- Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(shirt_size="large", shirt_text="I love Python"):
  print(f"Made a {shirt_size.upper()} shirt with the text {shirt_text} on it")

make_shirt()
make_shirt(shirt_size="medium")
make_shirt(shirt_size="small", shirt_text="I am still learning Python")
