#Created 12/06/2022
#Exercise 11-2- Population: Modify the function so the population parameter is optional. Run the test, and make sure test_city_country() passes again.
def get_city_country(city, country, population = ' '):
  return f"{city.title()}, {country.title()} - population {population}"
