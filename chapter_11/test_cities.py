import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    
    def test_city_country(self):
        test_city = city_country('beijing', 'china')
        self.assertEqual(test_city, 'Beijing, China')
        
    def test_city_country_population(self):
        test_city = city_country('beijing', 'china', 20000000)
        self.assertEqual(test_city, 'Beijing, China - population 20000000')
    
unittest.main()
