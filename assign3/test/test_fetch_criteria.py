import unittest
from src.fetch_criteria import fetch_a_criterion
from src.criteria.criteria_to_sort_name import criteria_to_sort_on as sort_name
from src.criteria.criteria_to_sort_city import criteria_to_sort_on as sort_city
from src.criteria.criteria_to_sort_city_name import criteria_to_sort_on as sort_city_name
from src.airport import Airport

class FetchCriteriaTests(unittest.TestCase):
    def setUp(self):
        self.iad = Airport("IAD", "DULLES INTL", "Washington", "DC", 71, True)
        
    def test_fetch_criteria_name(self):
        name_criterion = fetch_a_criterion("name")

        self.assertEqual(name_criterion(self.iad), sort_name(self.iad))
    
    def test_fetch_criteria_city(self):
        city_criterion = fetch_a_criterion("city")
        
        self.assertEqual(city_criterion(self.iad), sort_city(self.iad))
    
    def test_fetch_criteria_city_and_name(self):
        city_name_criterion = fetch_a_criterion("city and name")
        
        self.assertEqual(city_name_criterion(self.iad), sort_city_name(self.iad))
    
    def test_fetch_criteria_name_list(self):
        result = fetch_a_criterion("name_list")
        self.assertEqual(result, ["name"])
    
    def test_fetch_criteria_city_and_name_list(self):
        result = fetch_a_criterion("city_and_name_list")
        self.assertEqual(result, ["city and name"])

if __name__ == '__main__':
    unittest.main()
