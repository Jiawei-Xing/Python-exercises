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
