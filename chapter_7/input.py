message = input("What kind of car do you want? ")
print("Let me see if I can find you a " + message)

people = input("\nHow many people do you have? ")
people = int(people)
if people > 8:
    print("Sorry, we don't have enough seats.")
else:
    print("We have enough seats for you.")

number = input("\nPlease input a number: ")
number = int(number)
if number % 10 == 0:
    print("It can be divided by 10.")
else:
    print("It cannot be divided by 10.")
