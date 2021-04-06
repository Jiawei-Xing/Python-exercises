with open('guest.txt', 'w') as guest_file:
    guest = input("Name: ")
    guest_file.write(guest)
    
    
with open('guest_book.txt', 'a') as guest_book:
    while True:
        name = input('Name: ')
        if name == 'q':
            break
        else:
            print("Hello, " + name + "!")
            guest_book.write(name + "\n")

           
with open('reasons', 'a') as reasons:
    while True:
        reason = input("Why do you like programming?\n")
        if reason == 'q':
            break
        else:
            reasons.write(reason + "\n")
