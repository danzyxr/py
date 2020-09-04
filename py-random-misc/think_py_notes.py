import math
import random


def my_print(x):
    print(x)


def print_twice(x):
    print(x)
    print(x)


def for_each(iter, fn):
    for each in iter:
        fn(each)


def volume_sphere(r):
    return (4 / 3) * math.pi * (r ** 3)


def surface_sphere(r):
    return 4 * math.pi * (r ** 2)


def signal_noise(signal, noise):
    ratio = signal / noise
    decibels = 10 * math.log10(ratio)
    return decibels


def get_radians(degrees):
    radians = (degrees / 180.0) * math.pi
    return radians


def order_bulk(orders, discount, price):
    order_total = (price * discount) * orders
    shipping_cost = 3 + (0.75 * (orders - 1))
    grand_total = order_total + shipping_cost
    return grand_total


def right_justify(str):
    if len(str) < 70:
        builder = ""
        for i in range(70 - len(str)):
            builder += "+"
        return builder + str
    else:
        return str


def node_builder(n, x):
    builder = "+"
    builder += (" -" * n + " +") * x
    return builder


def column_builder(n, x):
    builder = "|"
    builder += ("  " * n + " |") * x
    # return (builder + "\n") * n
    return builder


def grid_builder(n, x):
    print(node_builder(n, x))
    for i in range(x):
        for i in range(n):
            print(column_builder(n, x))
        print(node_builder(n, x))


if __name__ == "__main__":
    li = [1, 3, 5]
    for_each(li, my_print)

    print(order_bulk(50, 0.4, 24.95))
    print(signal_noise(100, 10))
    print(math.sin(get_radians(45)))
    print(math.sqrt(2) / 2.0)

    degrees = 45.0
    x = math.sin(degrees / 360.0 * 2 * math.pi)

    print(math.exp(math.log(x)) + 1)
    print(math.exp(math.log(x + 1)))

    chords = [("G7", "GCDF"), ("Am7", "AEGC"), ("CMaj7", "CEGB")]

    c_major7 = chords[2]

    print_twice(c_major7[0])
    print_twice(random.choice(chords))

    chord_names = ["A minor 7", "C major 7", "G dominant 7"]

    for each_str in chord_names:
        tonic = each_str.split(" ")[0]

    print(right_justify("This line is now right-justified!"))

    grid_builder(1, 7)

    input("Press enter to exit...")

    exit()
