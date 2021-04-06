def city_country(city, country, population=''):
    if population:
        message = city.title() + ", " + country.title() + " - population " + str(population)
    else:
        message = city.title() + ", " + country.title()
    return message
