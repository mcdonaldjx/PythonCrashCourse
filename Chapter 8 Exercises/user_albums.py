#Created 11/23/2022 by Jared
#Exercise 8-8- User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album's artist and title. Once you have that information, call make_album() with the user's input and print the dictionary that's created. Be sure to include a quit value in the while loop. 
def make_album(artist, album_name):
  dict = {artist.title():album_name.title()}
  return dict
while True:
  artist = input("Enter an artist's name or enter q to quit: ")
  if artist == "q":
    break
  album_name = input(f"Enter an album made by {artist.title()} or enter q to quit: ")
  if album_name == "q":
    break
  print(f"{make_album(artist, album_name)}\n")
