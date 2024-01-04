# Q--> create a dictionary inside the dictionay and create a list inside the inner dictionary 
# first dictionary holds the countery
# the second dictionary holds the cities visited, to be visited , number of viditor, all of these three holds list cities visited, to be visited , number of viditor for there input value 

country_info = {}


country_info['France'] = {
    'cities_visited': ['Paris', 'Nice', 'Marseille'],
    'cities_to_visit': ['Lyon', 'Bordeaux', 'Toulouse'],
    'num_visitors': [50, 40, 30], 
    'dishes':{
        'popular_dishes': [ 'Pizza', 'spagetti'],
        'not_popular_dishes':['Nachos', 'hotdog']
    }
}

country_info['USA'] = {
    'cities_visited': ['New York', 'Los Angeles', 'Chicago'],
    'cities_to_visit': ['San Francisco', 'Miami', 'Las Vegas'],
    'num_visitors': [100, 150, 75]
}


print(country_info['France'])