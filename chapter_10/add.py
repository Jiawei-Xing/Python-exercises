while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        add = int(first_number) + int(second_number)
    except ValueError:
        print("Please input number only!")
    else:
        print(add)
