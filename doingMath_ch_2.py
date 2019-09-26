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

# range() is better here

for n in range(100):
    x_coords.append(n)
    y_coords.append(myFunction(n))

plt.plot(x_coords, y_coords, marker='o')
# plt.axis(xmin=0, xmax=100)
# plt.axis(ymin=0, ymax=10000)
# print(plt.axis())
plt.axis([0, 100, 0, 10000])
plt.show()
# plt.savefig('myFunction.png')

nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]

months = range(1, 13)
plt.plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
plt.legend([2000, 2006, 2012])
plt.xlabel('Months')
plt.ylabel('Temperature')
plt.title('NYC\'s Average Monthly Temperature')
# print(plt.axis())
# plt.axis(xmin=1, xmax=12)
# plt.axis(ymin=0, ymax=80)
plt.axis([1, 12, 0, 80])
plt.show()
# plt.savefig('NYC_temp.png')
