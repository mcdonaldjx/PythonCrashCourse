#Created 11/21/2022 by Jared
#Exercise 8-5- Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such asa Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city, country="the United States"):
  print(f"{city.title()} is in {country.title()}")
describe_city(city='houston')
describe_city(city='atlanta')
describe_city(city='paris', country='france')
