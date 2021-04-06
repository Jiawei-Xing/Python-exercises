class Restaurant():
  
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("\nName: " + self.restaurant_name.title())
        print("cuisine: " + self.cuisine_type.title())
        
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open.")
        
    def read_number_served(self):
        print("We have served " + str(self.number_served) + " people.")
        
    def set_number_served(self, number):
        self.number_served = number
        
    def increment_number_served(self, add_number):
        self.number_served += add_number
        
        
class IceCreamStand(Restaurant):
      
    def __init__(self, restaurant_name, cuisine_type, *flavor):
        super().__init__(restaurant_name, cuisine_type)
        self.flavor = flavor
        
    def print_flavor(self):
        print("\nFlavors: ")
        for flavor in self.flavor:
            print(flavor)
    
    
ice_cream = IceCreamStand('jw','chinese', 'a', 'b', 'c')
ice_cream.describe_restaurant()
ice_cream.open_restaurant()
ice_cream.set_number_served(3)
ice_cream.increment_number_served(4)
ice_cream.read_number_served()
ice_cream.print_flavor()


