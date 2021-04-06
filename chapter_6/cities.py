cities = {
    'Taiyuan': {'country': 'china', 'population': '400 million'},
    'Columbus': {'country': 'us', 'population': 'not much'},
    'Tokyo': {'country': 'Japan', 'population': 'a lot'},
    }

for city, information in cities.items():
    print("\n" + city + ":")
    for detail in information.values():
        print(detail)
