import unittest
from city_functions import city_country

class CityCountryTestCases(unittest.TestCase):
	"""Class which tests the functions of city_functions."""

	def test_city_country(self):
		"""Does the 'Santiago, Chile' work?"""
		formatted_city_country = city_country("santiago", "chile")
		self.assertEqual(formatted_city_country, "Santiago, Chile")


	def test_city_country_population(self):
		"""Does the 'Santiago, Chile - population 5000000' work?"""
		formatted_city_country_population = city_country("santiago", "chile", 5_000_000)
		self.assertEqual(formatted_city_country_population, "Santiago, Chile - population 5000000")


if __name__ == '__main__':
	unittest.main()
