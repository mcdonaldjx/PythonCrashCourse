#Created 11/21/2022 by Jared
#Exercise 8-3- T Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. 
#  Call the function once using positional arguments to make a shirt
#  Call the function a second time using keyword arguments

def make_shirt(shirt_Size, shirt_Text):
  print(f"Made a {shirt_Size.upper()} shirt with the text {shirt_Text} on it")

make_shirt("small", "this is a test shirt")
make_shirt(shirt_Size="medium", shirt_Text="I learned Python and all I got was this shirt")
