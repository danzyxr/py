import os
import json

list = []
path = "/home/dan/py/json/"
file = os.listdir(path)

for f in file:
    if f.endswith('.json'):
        list.append(path + f)

print(list)

for i in range(len(list)):
    with open(list[i]) as f:
        data = json.load(f)
        print(data)
