import calc

# A demonstration of calc.py


def compare_trajectory():
    while True:
        try:
            n = int(input("How many trajectories? "))
            if (type(n) == int) and (n > 0):
                break
            print("Enter a positive integer number")
        except Exception as e:
            print(e)
    for _ in range(n):
        while True:
            try:
                ivelo = float(input("Enter initial velocity (m/s): "))
                if ivelo > 0:
                    break
                print("Enter a positive number")
            except Exception as e:
                print(e)
        while True:
            try:
                angle = float(input("Enter initial velocity (m/s): "))
                if (angle > 0) and (angle < 180):
                    break
                print("Enter a positive number")
            except Exception as e:
                print(e)
        print(f"${n, ivelo, angle}")
        t_x, t_y, t_ax = calc.get_coords_trajectory(ivelo, angle)
        calc.draw_graph(t_x, t_y, t_ax)
    calc.show_graph()


if __name__ == "__main__":
    compare_trajectory()

    input("Press enter to quit...")
    quit()

    coe = [1, 2, 1]
    x_values = [-1, 1, 2, 3, 4, 5]
    y_values = []
    for n in x_values:
        y_values.append(calc.polynomial(n, coe))
    zipped = list(zip(x_values, y_values))
    print(f"Function values: {zipped}")

    input("Press enter to continue...")

    coeffs = [0.5, 2, 0.25]
    # coeffs = get_coeffs_poly()
    x, y, ax = calc.get_coords_poly(calc.polynomial, coeffs, 0, 100)
    calc.draw_graph(x, y, ax)
    calc.show_graph()

    g_x, g_y, g_ax = calc.get_coords_gravity(0.5, 1.5, calc.frange(1, 11, 0.1))
    calc.draw_graph(g_x, g_y, g_ax)
    calc.show_graph()

    t_x, t_y, t_ax = calc.get_coords_trajectory(25, 60)
    calc.draw_graph(t_x, t_y, t_ax)
    calc.show_graph()

    input("Press enter to quit...")
    quit()
