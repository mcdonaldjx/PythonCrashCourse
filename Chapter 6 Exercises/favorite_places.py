#Created 11/2/2022
#Exercise 6-9- Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store on to three favorite places for each person. Loop through the dictionary, and print each person's name and their favorite places.
favorite_places ={
  'jared': ['toronto', 'austin'],
  'kenni': ['cabo','austin'],
  'mari': ['brazil', 'atlanta']
}
for name in favorite_places:
  print(f"{name.title()}'s favorite places are:")
  for place in favorite_places[name]:
    print(f"\t{place.title()}")
