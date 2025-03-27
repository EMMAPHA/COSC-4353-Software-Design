import unittest
from src.process_airports import process_airports
from src.criteria.criteria_to_sort_iata import criteria_to_sort_on as sort_iata
from src.criteria.criteria_to_sort_name import criteria_to_sort_on as sort_name
from src.criteria.criteria_to_sort_city import criteria_to_sort_on as sort_city
from src.criteria.criteria_to_sort_state import criteria_to_sort_on as sort_state
from src.criteria.criteria_to_sort_delay import criteria_to_sort_on as sort_delay
from src.criteria.criteria_to_sort_temperature import criteria_to_sort_on as sort_temperature
from src.criteria.criteria_to_sort_city_name import criteria_to_sort_on as sort_city_name
from src.airport import Airport

class ProcessAirportTests(unittest.TestCase):
    def setUp(self):
        self.iad = Airport("IAD", "DULLES INTL", "Washington", "DC", 71, True)
        self.ord = Airport("ORD", "O'HARE INTERNATIONAL", "Chicago", "IL", 62, True)
        self.mdw = Airport("MDW", "MIDWAY INTERNATIONAL", "Chicago", "IL", 60, False)
        self.iah = Airport("IAH", "GEORGE BUSH INTERCONT.", "Houston", "TX", 82, True)
        self.sfo = Airport("SFO", "SAN FRANCISCO INTL.", "San Francisco", "CA", 59, False)
        self.lax = Airport("LAX", "LOS ANGELES INTL.", "Los Angeles", "CA", 84, False)
        self.hou = Airport("HOU", "HOBBY", "Houston", "TX", 80, False)

    def test_canary(self):
        self.assertTrue(True)

    def test_process_airports_empty(self):
        self.assertEqual(process_airports([]), [])

    def test_process_airports_single_airport(self):
        airports = [self.iad]
        
        self.assertEqual(process_airports(airports), airports)

    def test_process_airports_two_airports(self):
        airports = [self.iad, self.ord]
        
        self.assertEqual(process_airports(airports), airports)

    def test_process_airports_three_airports(self):
        airports = [self.iad, self.ord, self.mdw]
    
        self.assertEqual(process_airports(airports), airports)

    def test_process_two_airports_sort_by_iata(self):
        airports = [self.ord, self.mdw]
        
        sorted_airports = [self.mdw, self.ord]
        
        self.assertEqual(process_airports(airports, sort_key=sort_iata), sorted_airports)
        
    def test_process_three_airports_sort_by_name(self):
        airports = [self.iad, self.ord, self.mdw]
        
        sorted_airports = [self.iad, self.mdw, self.ord]
        
        self.assertEqual(process_airports(airports, sort_key=sort_name), sorted_airports)
        
    def test_process_three_airports_sort_by_city(self):
        airports = [self.iad, self.ord, self.mdw]
        
        sorted_airports = [self.ord, self.mdw, self.iad]
        
        self.assertEqual(process_airports(airports, sort_key=sort_city), sorted_airports)
        
    def test_process_three_airports_sort_by_delay(self):
        airports = [self.iad, self.ord, self.mdw]
        
        sorted_airports = [self.mdw, self.ord, self.iad]
        
        self.assertEqual(process_airports(airports, sort_key=sort_delay), sorted_airports)

    def test_process_three_airports_sort_by_state(self):
        airports = [self.iad, self.ord, self.mdw]
        
        sorted_airports = [self.iad, self.ord, self.mdw]
        
        self.assertEqual(process_airports(airports, sort_key=sort_state), sorted_airports)

    def test_process_three_airports_sort_by_temperature(self):
        airports = [self.iad, self.ord, self.mdw]
        
        sorted_airports = [self.mdw, self.iad, self.ord]
        
        self.assertEqual(process_airports(airports, sort_key=sort_temperature), sorted_airports)
        
    def test_process_three_airports_sort_by_city_and_name(self):
        airports = [self.ord, self.mdw, self.iad]
        
        sorted_airports = [self.mdw, self.ord, self.iad]
        
        self.assertEqual(process_airports(airports, sort_key=sort_city_name), sorted_airports)
        
    def test_process_lowercase_airports_names_in_uppercase(self): 
        aus = Airport("AUS", "Austin International", "Austin", "TX", 85, False)
    
        result = process_airports([aus])
        
        self.assertEqual(aus.name, "Austin International")
        self.assertEqual(result[0].name, "AUSTIN INTERNATIONAL")

if __name__ == '__main__':
    unittest.main()
     