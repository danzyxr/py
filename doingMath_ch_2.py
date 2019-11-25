import matplotlib.pyplot as plt

# plotting with
# cartesian coordinates

ax = []
x_coords = []
y_coords = []
coeffs = []


def linear(m, x, b):
    return (m*x) + b


def quadratic(x, coe):
    return (coe[0]*(x**2)) + (coe[1]*x) + coe[2]


def polynomial(x, coe):
    y = 0
    for i in range(0, (len(coe) - 1)):
        y = y + coe[i]*(x**(len(coe) - (1+i)))
    return coe[-1] + y


def get_coeffs_poly():
    coeffs.clear()
    n = int(input("Number of coefficients: "))
    for i in range(n):
        coeffs.append(float(input(f"Enter coefficient {i+1}: ")))
    print(coeffs)


def get_coords_poly(fn, lo, hi):
    x_coords.clear()
    y_coords.clear()
    for n in range(int(lo), int(hi+1)):
        x_coords.append(n)
        y_coords.append(fn(n, coeffs))
    ax.clear()
    ax.extend([lo, hi, fn(lo, coeffs), fn(hi, coeffs)])
    plt.title("Plot of polynomial function")
    plt.xlabel("x-values")
    plt.ylabel("y-values")


def draw_graph(x, y, ax):
    plt.plot(x, y, marker="o")
    plt.axis(ax)
    plt.show()


def gravity(m1, m2, r):
    G = 6.674e-11
    force = (G*(m1*m2))/(r**2)
    return force


def get_vars_gravity():
    m1 = float(input("Mass of object 1: "))
    m2 = float(input("Mass of object 2: "))
    r_i = int(input("Initial distance between them: "))
    r_f = int(input("Final distance between them: "))
    inc = int(input("Increments: "))
    r = range(r_i, (r_f+1), inc)
    return m1, m2, r


def get_coords_gravity():
    x_coords.clear()
    y_coords.clear()
    m1, m2, r = get_vars_gravity()
    for dist in r:
        f = gravity(m1, m2, dist)
        x_coords.append(dist)
        y_coords.append(f)
    ax.clear()
    ax.extend([x_coords[0], x_coords[-1], y_coords[-1], y_coords[0]])
    plt.title("Gravity between two massive objects")
    plt.xlabel("Distance in meters")
    plt.ylabel("Force in newtons")


# examples of matplotlib stuff

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
    # get_coeffs_poly()
    # get_coords_poly(polynomial, 0, 100)
    # draw_graph(x_coords, y_coords, ax)

    get_coords_gravity()
    draw_graph(x_coords, y_coords, ax)

    input("Press enter to quit...")
    quit()
