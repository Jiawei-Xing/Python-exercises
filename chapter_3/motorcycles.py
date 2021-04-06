# list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# add
motorcycles.append('honda')
print(motorcycles)

# delete
del motorcycles[-1]
print(motorcycles)
last_owned = motorcycles.pop(1)
print(motorcycles)
print("The last motorcycle I owned was a " + last_owned.title() + ".")
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
