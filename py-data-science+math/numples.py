import numpy as np


if __name__ == "__main__":
    ls = ["orange", "banana", 10, "leaf", 77.009, "tree", "cat"]

    print(f"List length: {len(ls)}")
    print(f"Cat count: {ls.count('cat')} & index: {ls.index('cat')}")
    print(ls)

    cat = ls.pop(ls.index("cat"))
    print(cat)

    ls.insert(0, "cat")
    ls.append(99)
    print(ls)

    ls[7] = "11"
    print(ls)

    ls.pop(1)
    print(ls)

    ls.pop()
    print(ls)

    print("\n")

    print("1st 3: ", ls[:3])
    print("Last 3: ", ls[-3:])
    print("3 before last (-1 excluded): ", ls[3:-1])
    print("Index 1 to 4 (5 excluded):", ls[1:5])
    print("Exclude edges: ", ls[1:-1])

    print("\n")

    fruit = ["orange"]
    more_fruit = ["apple", "peach", "kiwi"]
    fruit.extend(more_fruit)
    print(fruit)

    matrix = np.array([ls, fruit], dtype=object)
    print(matrix)

    print("1st row: ", matrix[0])
    print("2nd row: ", matrix[1])

    tumple = ("asdf", "qwerty", "42", 23, "nine", 3.333, 23)
    print(tumple, "has a lenght of: ", len(tumple))
    print(tumple, "has ", tumple.count(23), " twentythrees")

    print("\n")

    print("1st 3: ", tumple[:3])
    print("Last 3: ", tumple[-3:])
    print("3 before last (-1 excluded): ", tumple[3:-1])
    print("Index 1 to 4 (5 excluded):", tumple[1:5])
    print("Exclude edges: ", tumple[1:-1])

    print("\n")

    nu_matrix = np.array([list(tumple), matrix[0], matrix[1]], dtype=object)
    print(nu_matrix)

    print("\n")

    smoothie_recipe = {
        "milk": "1 cup",
        "banana": "100 gram",
        "blueberry": "100 gram",
        "coconut": "100 gram",
        "yogurt": "1 cup",
    }

    print(smoothie_recipe)
    del smoothie_recipe["coconut"]
    smoothie_recipe["strawberry"] = "100 gram"
    dict_ls = [smoothie_recipe]

    tropical_recipe = {
        "milk": "1 cup",
        "mango": "100 gram",
        "pineapple": "100 gram",
        "coconut": "100 gram",
        "yogurt": "1 cup",
    }

    dict_ls.append(tropical_recipe)
    print(dict_ls)

    print("\n")

    for i, row in enumerate(dict_ls):
        print("row", i, ":")
        print(row)
