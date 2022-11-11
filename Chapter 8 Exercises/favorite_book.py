#Created 11/10/2022 by Jared
#Exercise 8.2- Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in wonderland. Call the funciton, making sure to include a book title as an argument in the function call.
def favorite_book(title):
  """This function prints the title of my favorite book."""
  print(f"One of my favorite books is {title.title()}")

book_title = input("What is the title of your favorite book? ")
favorite_book(book_title)
