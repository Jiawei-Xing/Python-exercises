class ElectricCar():
    
    def __init__(self):
        self.battery = Battery()
        
        
class Battery():
    
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
        
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
            
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        print(range)
            
car = ElectricCar()
car.battery.upgrade_battery()
car.battery.get_range()
