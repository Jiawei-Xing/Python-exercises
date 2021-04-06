with open('origin_of_species.txt') as book:
    content = book.read()

count = content.lower().count('the')
print(count)

words = content.split()
number = len(words)
print(number)

print(count/number)
