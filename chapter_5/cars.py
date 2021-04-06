cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

print("\nIs 'audi' in cars? I predict True.")
print('audi' in cars)

print("\nIs 'GeGe' in cars? I predict False.")
print('GeGe' in cars, "\n")

print(1 != 2)
