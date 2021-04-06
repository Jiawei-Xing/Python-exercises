def make_car(maker, type, **info):
    cars = {'maker': maker, 'type': type}
    for key, value in info.items():
        cars[key] = value
    return cars
    
car = make_car('sabaru', 'outback', color='blue', two_package=True)
print(car)
