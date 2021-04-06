numbers = {
    'Jiawei': [8,9,10], 
    'Gege': [7], 
    'gaga': [6,0], 
    'gigi': [5], 
    'gugu': [4], 
    }

for name, number in numbers.items():
    print("\n" + name + ": ")
    for each_number in number:
        print(str(each_number))
        
