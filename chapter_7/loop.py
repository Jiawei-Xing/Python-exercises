toppings = ()
while toppings != 'quit':
    toppings = input("\nPlease input toppings (Enter 'quit' to finish): ")
    if toppings != 'quit':
        print("We will add " + toppings + " to your pizza.")

active = True
while active:
    age = input("\nPlease input your age: ")
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 0:
            print("Please input a valid age!")
        elif age < 3:
            print("free")
        elif age <= 12:
            print("$10")
        else:
            print("$15")
