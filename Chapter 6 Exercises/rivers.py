#Created 11/1/2022
#Exercise 6-5- Rivers: Make a dictionary containing three major rivers and the country each river runs throught.
#  Use a for loop to print a sentence about each river
#  Use a loop to print the name of each river included in the dictionary
#  Use a loop to print the name of each country included in the dictionary
rivers = {'nile':'egypt', 'mississippi':'usa', 'amazon':'peru'}
for river,country in rivers.items():
  print(f"The {river.title()} River flows through {country.title()}")
print("\nRivers in the dictionary:")
for river in rivers.keys():
  print(f"\t{river.title()} River")
print("Countries in the dictionary:")
for country in rivers.values():
  print(f"\t{country.title()}")
