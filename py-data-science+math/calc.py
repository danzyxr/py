import math
import matplotlib.pyplot as plt

# UI + Visualiser
# Exception handling


def linear(m, x, b):
    return (m * x) + b


def quadratic(x, coe):
    return (coe[0] * (x ** 2)) + (coe[1] * x) + coe[2]


def solve_quadratic(a, b, c):
    D = (b * b) - (4 * a * c)
    x_1 = (-b + math.sqrt(D)) / (2 * a)
    x_2 = (-b - math.sqrt(D)) / (2 * a)
    roots = (x_1, x_2)
    return roots


def polynomial(x, coe):
    y = 0
    for i in range(0, (len(coe) - 1)):
        y = y + coe[i] * (x ** (len(coe) - (i + 1)))
    return y + coe[-1]


def get_coeffs_poly():
    coeffs = []
    n = int(input("Number of coefficients: "))
    for i in range(n):
        coeffs.append(float(input(f"Enter coefficient {i + 1}: ")))
    return coeffs


def get_coords_poly(fn, coeffs, lo, hi):
    x = []
    y = []
    for n in range(int(lo), int(hi + 1)):
        x.append(n)
        y.append(fn(n, coeffs))
    ax = []
    ax.extend([min(x), max(x), min(y), max(y)])
    # ax.extend([lo, hi, fn(lo, coeffs), fn(hi, coeffs)])
    plt.title("Plot of polynomial function")
    plt.xlabel("x-values")
    plt.ylabel("y-values")
    return x, y, ax


def factor(a, b):
    if (b % a) == 0:
        # print(f"{a} is a factor of {b}")
        return a


def all_factors(x):
    i = 1
    factor_list = []
    while i <= x:
        if isinstance(factor(i, x), int):
            factor_list.append(factor(i, x))
        i = i + 1
    # print(f"Factors of {x} are {factor_list}")
    return factor_list


def gravity(m1, m2, r):
    G = 6.674e-11
    force = (G * (m1 * m2)) / (r ** 2)
    return force


def get_coords_gravity(m1, m2, r):
    x = []
    y = []
    for dist in r:
        f = gravity(m1, m2, dist)
        x.append(dist)
        y.append(f)
    ax = []
    ax.extend([min(x), max(x), min(y), max(y)])
    plt.title(f"Gravity between {m1}kg & {m2}kg")
    plt.xlabel("Distance in meters")
    plt.ylabel("Force in newtons")
    return x, y, ax


def frange(i, f, inc):
    n = []
    while i < f:
        n.append(i)
        i = i + inc
    return n


def get_coords_trajectory(u, theta):
    g = 9.8
    rads = math.radians(theta)
    t_flight = 2 * u * math.sin(rads) / g
    t_intervals = frange(0, t_flight, 0.001)
    x = []
    y = []
    for t in t_intervals:
        x.append(u * math.cos(rads) * t)
        y.append(u * math.sin(rads) * t - 0.5 * g * t * t)
    ax = []
    ax.extend([min(x), max(x), min(y), max(y)])
    plt.title(f"Object trajectory @ {u}m/s & {theta} degrees")
    plt.xlabel("Distance traveled [m]")
    plt.ylabel("Height reached [m]")
    return x, y, ax


def draw_graph(x, y, ax):
    plt.axis(ax)
    plt.plot(x, y, marker="o")
    plt.show()


if __name__ == "__main__":
    pass
