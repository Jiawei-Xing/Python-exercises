def show_magicians(magicians):
    for magician in magicians:
        print(magician)

# ~ def make_great(magicians):
    # ~ new_magicians = []
    # ~ for magician in magicians:
        # ~ new_magician = magician + " the Great"
        # ~ new_magicians.append(new_magician)
    # ~ return new_magicians
    
# ~ magicians = ['Jiawei', 'Sb', 'Gege']
# ~ show_magicians(magicians)
# ~ show_magicians(make_great(magicians))
    

def make_great(magicians):
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magician = magician + " the Great"
        great_magicians.append(great_magician)
    return great_magicians

magicians = ['Jiawei', 'Sb', 'Gege']
great_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)
