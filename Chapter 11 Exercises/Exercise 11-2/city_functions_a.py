#Created 12/06/2022
#Exercise 11-2- Population: Modify your function so it requires a third parameter, population. It should now return a single string of the form City, Country – population xxx, such as Santiago, Chile – population 5000000. Run the test again, and make sure test_city_country() fails this time.
def get_city_country(city, country, population):
  return f"{city.title()}, {country.title()} - population {population}"
