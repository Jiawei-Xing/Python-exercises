my_foods = ['pizza', 'gege', 'gaga']
his_foods = my_foods[:]
my_foods.append('cake')
print(my_foods)
his_foods.append('bread')
print(his_foods,"\n")

for food in my_foods:
	print(food)
print("\n")
for food in his_foods:
	print(food)
