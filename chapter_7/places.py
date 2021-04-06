greeting = "\nHello, what's your name? "
message = "If you could visit one place in the world, where would you go? "
places = {}

while True:
    name = input(greeting)
    place = input(message)
    places[name] = place
    repeat = input("\tWould you like to add another one? ")
    if repeat == 'no': 
        break

for name, place in places.items():
    print("\n" + name.title() + " wants to visit " + place + ".")
