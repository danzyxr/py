import matplotlib.pyplot as plt

# plotting with
# cartesian coordinates

ax = []
x_coords = []
y_coords = []
coeffs = []


def quadratic(x, coe):
    return (coe[0]*(x**2)) + (coe[1]*x) + coe[2]


def get_coeffs():
    coeffs.clear()
    n = int(input("Number of coefficients: "))
    for i in range(n):
        coeffs.append(input(f"Enter coefficient {i+1}: "))
    print(coeffs)


def get_coords(fn, lo, hi):
    lo = int(lo)
    hi = int(hi)
    x_coords.clear()
    y_coords.clear()
    for n in range(lo, hi):
        x_coords.append(n)
        y_coords.append(fn(n, coeffs))
    ax.clear()
    ax.extend([lo, hi, fn(lo, coeffs), fn(hi, coeffs)])


def draw_graph(x, y, ax):
    plt.plot(x, y, marker="o")
    plt.axis(ax)
    plt.show()


# plt.plot(x_coords, y_coords, marker='o')
# plt.axis(xmin=0, xmaxes=100)
# plt.axis(ymin=0, ymaxes=10000)
# print(plt.axis())
# plt.axis([0, 100, 0, 10000])
# plt.savefig('myFunction.png')
# plt.show()

# nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
# nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
# nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]

# months = range(1, 13)
# plt.plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
# plt.legend([2000, 2006, 2012])
# plt.xlabel('Months')
# plt.ylabel('Temperature')
# plt.title('NYC\'s Average Monthly Temperature')
# print(plt.axis())
# plt.axis(xmin=1, xmaxes=12)
# plt.axis(ymin=0, ymaxes=80)
# plt.axis([1, 12, 0, 80])
# plt.savefig('NYC_temp.png')
# plt.show()

if __name__ == "__main__":
    get_coeffs()
    get_coords(quadratic, -100, 100)
    draw_graph(x_coords, y_coords, ax)
    input("Press enter to quit...")
    quit()
