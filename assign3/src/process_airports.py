from dataclasses import replace

def process_airports(airports, sort_key=lambda airport: ()):
    def uppercase_airport_name(airport):
        return replace(airport, name=airport.name.upper())
    
    return sorted(map(uppercase_airport_name, airports), key=sort_key)
    