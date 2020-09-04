diction = {"brand": "Ford", "model": "Fiesta ST", "year": 2015}

print(list(diction.items()))
print(list(zip(diction.keys(), diction.values())))
print([(k, v) for k, v in diction.items()])

list_dict = []
for key in diction:
    t = (key, diction[key])
    list_dict.append(t)
print(list_dict)
