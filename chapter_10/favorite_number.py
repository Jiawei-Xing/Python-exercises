# ~ import json

# ~ filename = 'favorite_number.json'
# ~ try: 
    # ~ with open(filename) as file_object:
        # ~ read_number = json.load(file_object)
# ~ except FileNotFoundError:
    # ~ favorite_number = input("favorite number: ")
    # ~ with open(filename, 'w') as file_object:
        # ~ json.dump(favorite_number, file_object)
# ~ else:
    # ~ print("I know your favorite number is " + read_number)


import json

def store_new_number():
    favorite_number = input("favorite number: ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as file_object:
        json.dump(favorite_number, file_object)
    
def get_stored_number():
    filename = 'favorite_number.json'
    try: 
        with open(filename) as file_object:
            read_number = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return read_number
        
def greet_user():
    favorite_number = get_stored_number()
    new = input('Are you new or old user? ')
    if new == 'old' and favorite_number:
        print("We know your favorite number is " + favorite_number)
    else:
        store_new_number()
        print("We will remember your favorite number!")

greet_user()
