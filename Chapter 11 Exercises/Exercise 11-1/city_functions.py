#Created 12/06/2022
#Exercise 11-1- Write a function that accepts two parameters: a city name and a country name. The function should return a single string of the form City, Country, such as Santiago, Chile. Store the function in a module called city_functions.py. Create a file called test_cities.py that tests the function you just wrote. Write a function called test_city_country() to verify that calling your function with values such as 'santiago' and 'chile' results in the correct string. Run the test, and make sure test_city_country() passes.
def get_city_country(city, country):
  return f"{city.title()}, {country.title()}"
