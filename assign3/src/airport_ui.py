import sys
from airport import Airport
from process_airports import process_airports
from fetch_criteria import fetch_a_criterion

def load_airports(filename):
    airports = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                iata_code, name, city, state, temperature, delay = line.strip().split(',')
                temperature = int(temperature)
                delay = delay == 'True'
                airports.append(Airport(iata_code, name, city, state, delay, temperature))
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1) 
    except Exception as e:
        print(f"An error occurred while loading airports: {e}")
        sys.exit(1)

    return airports

def display_airports(airports):
    for airport in airports:
        print(f"IATA Code: {airport.iata_code}, Name: {airport.name}, "
              f"City: {airport.city}, State: {airport.state}, "
              f"Temperature: {airport.temperature}°F, Delay: {airport.delay}")

def main(filename):
    airports = load_airports(filename)
    
    criteria_options = {
        "0": "none",
        "1": "iata_code",
        "2": "name",
        "3": "city",
        "4": "state",
        "5": "delay",
        "6": "temperature",
        "7": "city and name"
    }

    print("Choose a sorting criterion:")
    for key, value in criteria_options.items():
        print(f"{key}. {value.replace('_', ' ').title()}")

    choice = input("Enter your choice (0-7): ")
    
    if choice not in criteria_options:
        print("Invalid choice. Defaulting to 'none' (no sorting).")
        property_name = "none"
    else:
        property_name = criteria_options[choice]

    if property_name == "none":
        sorted_airports = process_airports(airports)
    else:
        sort_key = fetch_a_criterion(property_name)
        sorted_airports = process_airports(airports, sort_key)

    print("\nSorted Airports:")
    display_airports(sorted_airports)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python airport_ui.py <filename>")
    else:
        main(sys.argv[1])
