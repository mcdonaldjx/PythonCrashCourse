def test_city_country_population(self):
  result = get_city_country('santiago', 'chile', '5000000')
  assert result == 'Santiago, Chile - population 5000000'
