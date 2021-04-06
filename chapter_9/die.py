from random import randint

"""roll die with different sides randomly"""
class Die():
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self):
        self.number = randint(1, self.sides)
        print(self.number)
        
 # 6 sides       
# ~ number = Die()
# ~ number.roll_die()
# ~ number.roll_die()
# ~ number.roll_die()
# ~ number.roll_die()
# ~ number.roll_die()
# ~ number.roll_die()
# ~ number.roll_die()
# ~ number.roll_die()
# ~ number.roll_die()
# ~ number.roll_die()

# 10 sides
# ~ number = Die(10)
# ~ number.roll_die()
# ~ number.roll_die()
# ~ number.roll_die()
# ~ number.roll_die()
# ~ number.roll_die()
# ~ number.roll_die()
# ~ number.roll_die()
# ~ number.roll_die()
# ~ number.roll_die()
# ~ number.roll_die()

#20 sides
number = Die(20)
number.roll_die()
number.roll_die()
number.roll_die()
number.roll_die()
number.roll_die()
number.roll_die()
number.roll_die()
number.roll_die()
number.roll_die()
number.roll_die()
