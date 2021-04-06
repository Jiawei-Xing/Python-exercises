information = {'first_name': 'Jiawei', 'last_name': 'Xing', 'age': '22', 
    'city': 'Columbus'}
print(information['first_name'])
print(information['last_name'])
print(information['age'])
print(information['city'])

numbers = {
    'Jiawei': 8, 
    'Gege': 7, 
    'gaga': 6, 
    'gigi': 5, 
    'gugu': 4, 
    }
print("\nJiawei " + str(numbers['Jiawei']))
print("Gege " + str(numbers['Gege']))
print("gaga " + str(numbers['gaga']))
print("gigi " + str(numbers['gigi']))
print("gugu " + str(numbers['gugu']))

python_words = {'\t': 'tab', '\n': 'newline', 'strip': 'delete spaces', 
    '#': 'annotation', 'sorted': 'temporary sort'}
print("\ t\n\t" + python_words['\t'])
print("\ n\n\t" + python_words['\n'])
print("strip\n\t" + python_words['strip'])
print("#\n\t" + python_words['#'])
print("sorted\n\t" + python_words['sorted'])

for word, function in python_words.items():
    print("\nword\t" + word + "\nfunction\t" + function)


