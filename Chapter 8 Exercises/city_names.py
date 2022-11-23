#Created 11/23/2022 by Jared
#Exercise 8-6- City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like: "City, Country"
#  Call your function with at least three city-country pairs, and print the values that are returned.
def city_country(city,country):
  city_country = f"{city.title()}, {country.title()}"
  return city_country
print(city_country("houston","united states of america"))
print(city_country("paris","france"))
print(city_country("toronto","canada"))
