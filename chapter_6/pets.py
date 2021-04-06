Lele = {'type': 'dog', 'owner': 'Jiawei'}
Miaomiao = {'type': 'cat', 'owner': 'Chang'}
pets = [Lele, Miaomiao]

for pet in pets:
    print("\ntype: " + pet['type'] + "\nowner: " + pet['owner'].title())
