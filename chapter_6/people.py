information_1 = {'first_name': 'Jiawei', 'last_name': 'Xing', 'age': '22', 
    'city': 'Columbus'}
information_2 = {'first_name': 'j', 'last_name': 'X', 'age': '2', 
    'city': 'us'}
information_3 = {'first_name': 'wei', 'last_name': 'ing', 'age': '222', 
    'city': 'Cous'}
people = [information_1, information_2, information_3]

for information in people:
    full_name = information['first_name'].title() + " " + information['last_name'].title()
    print("\nfull name: " + full_name + "\nage: " + information['age'] 
    + "\ncity: " + information['city'])
    
