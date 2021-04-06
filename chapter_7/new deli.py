sandwich_orders = ['a', 'pastrami', 'b', 'c', 'pastrami', 'pastrami']
print("We don't have pastrami now.")
# delete redundancy
sandwich_orders = set(sandwich_orders)
# delete all 'pastrami'
sandwich_orders.remove('pastrami')
print(sandwich_orders, "\n")

finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print("I made your " + sandwich + " sandwich.")
    
print("\nThese sandwiches are finished:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
