#Created 11/2/2022
#Exercise 6-11- Cities: Make a dictionary called cities. se the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, it approximate population, and one fact about that city. The keys for each city's dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
cities = {
  'toronto':{'country': 'canada', 'population':2794356, 'fact':'toronto has over 10 million trees', 'area code': 416},
  'houston':{'country':'united states', 'population':2304580, 'fact':'houston is the most ethnically diverse metropolitan area in the united states', 'area code': 281},
  'austin':{'country':'united states', 'population':964177, 'fact':'austin was originally called the waterloo', 'area code':512}
}
for city, stat in cities.items():
  print(f"Facts about {city.title()}:")
  country = stat['country']
  population = stat['population']
  fun_fact = stat['fact']
  area_code = stat['area code']
  print(f"\tLocated in {country.title()}")
  print(f"\tPopulation of {population} people")
  print(f"\tFun fact: {fun_fact}")
  print(f"\tArea Code is {area_code}")
