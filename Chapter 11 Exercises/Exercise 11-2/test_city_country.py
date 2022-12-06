def test_city_country(self):
  result = get_city_country('santiago','chile')
  assert result == 'Santiago, Chile - population  '
