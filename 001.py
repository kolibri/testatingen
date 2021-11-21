cities = ['Hamburg', 'Hamburg', 'Berlin', 'Köln', 'Neuss']

# create list with unique entries only
unique_cities = list(set([city for city in cities]))
#unique_cities = {city for city in cities}

print("Unique cities: ")
print(unique_cities)


print("\n")
# define some state with capital cities
states = {'Nordrhein-Westfalen': 'Düsseldorf', 'Berlin': 'Berlin', 'Bayern': 'München'}

states_to_check = ['Nordrhein-Westfalen', 'Berlin', 'Baden-Württemberg', 'Düsseldorf', 'Deutschland']

print("\n")
print("Check for states")
for state in states.keys():
  if state in states_to_check:
    print(state + " exists in states_to_check")

cities_to_check = ['Düsseldorf', 'München', 'Berlin', 'Baden-Württemberg', 'Frankreich']

print("\n")
print("Check for cites")
for city in states.values():
  if city in cities_to_check:
    print(city + " exists in states_to_check")





