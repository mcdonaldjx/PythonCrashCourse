#Created 11/29/2022 by Jared
def make_album(artist, album_name, num_of_songs=None):
  dict = {artist.title():album_name.title()}
  if num_of_songs:
    dict[album_name.title()] = num_of_songs
  return dict
