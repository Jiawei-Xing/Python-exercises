pizzas = ['pepperoni', 'cheese', 'Hawaii']
for pizza in pizzas:
	print("I like " + pizza + " pizza.")

print("I really like pizza!\n")

friend_pizzas = pizzas[:]
pizzas.append('apple')
friend_pizzas.append('banana')
print("My favorite pizzas are: ")
for pizza in pizzas:
	print(pizza)
print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
	print(pizza)
