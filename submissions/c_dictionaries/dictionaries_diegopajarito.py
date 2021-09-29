cities = {'last_1': 'Bogota', 'last_2': 'Duitama', 'last_3': 'Medellin', 'last_4': 'Barcelona', 'last_5': 'Lisbon'}

print(cities)

cities = { 'Barcelona': {'population': 5474482, 'unemployment_rate': 17.24},
           'lisbon': {'population': 2827514, 'unemployment_rate': 7.4},
           'Amsterdam': {'population': 2431000, 'unemployment_rate': 3.3} }


cities['Bogota'] = {'population': 7450987, 'unemployment_rate': 11.3}

print(cities)

keys = cities.keys()
for city in keys:
    print(cities[city])
