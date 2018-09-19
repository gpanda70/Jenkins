import os

filename = (os.path.join(os.path.dirname(__file__), 'command.txt'))
print(filename)
content = []
with open(filename) as f:
    for line in f:
        content.append(line.rstrip('\r\n'))
        print(content)
