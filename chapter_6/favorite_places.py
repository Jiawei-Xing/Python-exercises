favorite_places = {
    'Jiawei': ['Qingdao', 'SF'], 
    'Gege': ['Beijing'], 
    'Zhao': ['Qinhuadao']
    }

for name, place in favorite_places.items():
    if len(place) != 1:
        print("\n" + name.title() + "'s favorite places are: ")
    else: 
        print("\n" + name.title() + "'s favorite place is: ")
    for place_name in place:
        print(place_name)
