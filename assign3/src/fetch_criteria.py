def fetch_a_criterion(property_name):
    if property_name == "city_and_name_list": 
        return ["city and name"]
    
    if property_name == "name_list": 
        return ["name"]
    
    if property_name in ["iata_code", "name", "city", "state", "delay", "temperature"]: 
        return lambda airport: getattr(airport, property_name)
    
    if property_name == "city and name": 
        return lambda airport: (airport.city, airport.name)
