# Create a dictionary to store information about countries
country_info = {}

# Add information for the first country
country_info['USA'] = {
    'cities_visited': ['New York', 'Los Angeles', 'Chicago'],
    'cities_to_visit': ['San Francisco', 'Miami', 'Las Vegas'],
    'num_visitors': [100, 150, 75]
}

# Add information for the second country
country_info['France'] = {
    'cities_visited': ['Paris', 'Nice', 'Marseille'],
    'cities_to_visit': ['Lyon', 'Bordeaux', 'Toulouse'],
    'num_visitors': [50, 40, 30]
}

# Add information for more countries as needed

# Access and print information for a specific country
print("Information for USA:")
print("Cities Visited:", country_info['USA']['cities_visited'])
print("Cities to Visit:", country_info['USA']['cities_to_visit'])
print("Number of Visitors:", country_info['USA']['num_visitors'])
