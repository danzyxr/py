import matplotlib.pyplot as plt

# myList = [1, 2, 3]
# for item in myList:
#     print(item)

# for index, item in enumerate(myList):
#     print(index, item)

# myTuple = (4, 5, 6)
# for item in myTuple:
#     print(item)

# for index, item in enumerate(myTuple):
#     print(index, item)


def myFunction(x):
    return (3*(x**2)) + (6*x) + 9


x_coords = []
y_coords = []

# n = 1
# while True:
#     x_coords.append(n)
#     y_coords.append(myFunction(n))
#     if n == 10:
#         break
#     n = n + 1

for i in range(100):
    x_coords.append(i)
    y_coords.append(myFunction(i))

plt.plot(x_coords, y_coords, marker='o')
plt.show()
