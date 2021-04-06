accounts = []
if accounts:
    for account in accounts:
        if account == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + account + ", thanks for logging in again.")
else:
    print("We need to find some users!\n")

current_users = ['a', 'b', 'c', 'd', 'E']
new_users = ['D', 'e', 'f', 'g', 'h']
current_users = [user.lower() for user in current_users]
for user in new_users:
    if user.lower() in current_users:
        print("Please input something else.")
    else:
        print("It's not used.")
print(current_users)
print(new_users)
