import math
import matplotlib.pyplot as plt

# Plotting with
# Cartesian coordinates
# Don't use global lists!!
# Make purely functional


def linear(m, x, b):
    return (m*x) + b


def quadratic(x, coe):
    return (coe[0]*(x**2)) + (coe[1]*x) + coe[2]


def polynomial(x, coe):
    y = 0
    for i in range(0, (len(coe) - 1)):
        y = y + coe[i]*(x**(len(coe) - (i + 1)))
    return coe[-1] + y


def get_coeffs_poly():
    coeffs = []
    n = int(input("Number of coefficients: "))
    for i in range(n):
        coeffs.append(float(input(f"Enter coefficient {i + 1}: ")))
    return coeffs


def get_coords_poly(fn, coeffs, lo, hi):
    x = []
    y = []
    for n in range(int(lo), int(hi+1)):
        x.append(n)
        y.append(fn(n, coeffs))
    ax = []
    ax.extend([min(x), max(x), min(y), max(y)])
    # ax.extend([lo, hi, fn(lo, coeffs), fn(hi, coeffs)])
    plt.title("Plot of polynomial function")
    plt.xlabel("x-values")
    plt.ylabel("y-values")
    return x, y, ax


def draw_graph(x, y, ax):
    plt.axis(ax)
    plt.plot(x, y, marker="o")
    plt.show()


def gravity(m1, m2, r):
    G = 6.674e-11
    force = (G*(m1*m2))/(r**2)
    return force


'''
def get_vars_gravity():
    m1 = float(input("Mass of obj 1 (in tonnes): ")) * 1000
    m2 = float(input("Mass of obj 2 (in tonnes): ")) * 1000
    r = range(1, 101, 1)
    return m1, m2, r
'''


def get_coords_gravity(m1, m2, r):
    x = []
    y = []
    # m1, m2, r = get_vars_gravity()
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
    plt.ylabel("Height reached")
    plt.xlabel("Ground traveled")
    return x, y, ax


if __name__ == "__main__":
    coeffs = [0.5, 2, 0.25]
    # coeffs = get_coeffs_poly()
    x, y, ax = get_coords_poly(polynomial, coeffs, 0, 100)
    draw_graph(x, y, ax)

    g_x, g_y, g_ax = get_coords_gravity(0.5, 1.5, frange(1, 11, 0.1))
    draw_graph(g_x, g_y, g_ax)

    t_x, t_y, t_ax = get_coords_trajectory(25, 60)
    draw_graph(t_x, t_y, t_ax)

    input("Press enter to quit...")
    quit()
