file_name = 'learning_python.txt'

with open(file_name) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())
  
with open(file_name) as file_object:
    lines = file_object.readlines()

info = ''
for line in lines:
    info += line
    
print(info)


# replace python with C

with open(file_name) as file_object:
    lines = file_object.readlines()
    # ~ print(lines)
    for line in lines:
        print(line.replace('python', 'C'))
        # ~ print(line.rstrip())
        
# ~ message = "I really like dogs."
# ~ print(message.replace('dog', 'cat'))
# ~ print(message)
