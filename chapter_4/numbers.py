for value in range(1,11):
	print(value)
numbers = list(range(1,11,3))
print(numbers)
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)
print(max(squares))
print(min(squares))
print(sum(squares))
squares = [value**2 for value in range(1,11)]
print(squares,"\n")

for value in range(1,21):
	print(value)

for value in range(1,10):
	print(value)
	
numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1,20,2))
for value in odd_numbers:
	print(value)

three_numbers = list(range(3,31,3))
for value in three_numbers:
	print(value)

cube = [value**3 for value in range(1,11)]
print(cube)
for value in cube:
	print(value)

cubes = []
for value in range(1,11):
	cubes.append(value**3)
print(cubes)

print("The first three items in the list are: ")
for value in cubes[-3:]:
	print(value)
