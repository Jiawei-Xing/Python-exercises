# ~ try:
    # ~ with open('cats.txt') as cats:
        # ~ cat = cats.read()
# ~ except FileNotFoundError:
    # ~ print("Cannot found file cats.txt!")
# ~ else:
    # ~ print(cat)
    
# ~ try:
    # ~ with open('dogs.txt') as dogs:
        # ~ dog = dogs.read()
# ~ except FileNotFoundError:
    # ~ pass
# ~ else:
    # ~ print(dog)
    

def print_files(filename):
    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(content)
        
filename = ['cats.txt', 'dogs.txt']
for each_file in filename:
    print_files(each_file)
