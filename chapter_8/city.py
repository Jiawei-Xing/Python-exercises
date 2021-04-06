def describe_city(name, country = 'china'):
    print(name.title() + " is in " + country.title())

describe_city('taiyuan')
describe_city('beijing')
describe_city('columbus', 'united states')

def city_country(city, country):
    message = '\n"' + city.title() + ", " + country.title() + '"'
    return message
    
city = city_country('Taiyuan', 'china')
print(city)
city = city_country('Columbus', 'united states')
print(city)
city = city_country('tokyo', 'japan')
print(city)
