import os
import json

list = []
path = "C:/Users/dan/Desktop/fcc-notes/css/"
file = os.listdir(path)

for f in file:
    if f.endswith(".json"):
        list.append(path + f)

for each in list:
    print(each)

for i in range(len(list)):
    with open(list[i]) as f:
        data = json.load(f)
        print("\n", data)

quit()
