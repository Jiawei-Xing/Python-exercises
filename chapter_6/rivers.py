rivers = {'nile': 'egypt', 'yellow': 'china', 'ohio': 'united states'}
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

visited_rivers = ['yellow', 'ohio']
for river in rivers.keys():
    if river in visited_rivers:
        print("I have visited the " + river.title() + ".")
    else:
        print("Please visit the " + river.title() + ".")
