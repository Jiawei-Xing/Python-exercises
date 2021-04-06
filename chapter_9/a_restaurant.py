from restaurant import Restaurant

restaurant = Restaurant('jw','chinese')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(3)
restaurant.increment_number_served(4)
restaurant.read_number_served()


# ~ class Dog():
    
    # ~ def __init__(self, name, age):
        # ~ self.name = name
        # ~ self.age = age
        
    # ~ def sit(self):
        # ~ print(self.name.title() + " is now sitting.")
        
    # ~ def roll_over(self):
        # ~ print(self.name.title() + " rolled over!")
        

# ~ my_dog = Dog('willie', 6)
# ~ my_dog.sit()
# ~ my_dog.roll_over()
