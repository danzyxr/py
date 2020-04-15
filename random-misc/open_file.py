with open('random-misc/open_me.txt', 'r') as f:
    content = f.readlines()

content = [line.strip() for line in content]

for line in content:
    print(line)
