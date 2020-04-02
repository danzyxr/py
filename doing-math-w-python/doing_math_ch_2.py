import matplotlib.pyplot as plt

# Plotting with
# Cartesian coordinates
# Don't use global lists!!


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
    ax.extend([lo, hi, fn(lo, coeffs), fn(hi, coeffs)])

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


def get_vars_gravity():
    m1 = float(input("Mass of obj 1 (in tonnes): ")) * 1000
    m2 = float(input("Mass of obj 2 (in tonnes): ")) * 1000
    r = range(1, 101, 1)
    return m1, m2, r


def get_coords_gravity():
    x = []
    y = []
    m1, m2, r = get_vars_gravity()
    for dist in r:
        f = gravity(m1, m2, dist)
        x.append(dist)
        y.append(f)
    ax = []
    ax.extend([x[0], x[-1], y[-1], y[0]])
    plt.title("Gravity between two massive objects")
    plt.xlabel("Distance in meters")
    plt.ylabel("Force in newtons")
    return x, y, ax


if __name__ == "__main__":
    coeffs = get_coeffs_poly()
    x, y, ax = get_coords_poly(polynomial, coeffs, 0, 100)
    draw_graph(x, y, ax)

    g_x, g_y, g_ax = get_coords_gravity()
    draw_graph(g_x, g_y, g_ax)

    input("Press enter to quit...")
    quit()
