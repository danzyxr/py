import math
from fractions import Fraction


def types():
    print(type(369))
    print(type(math.pi))
    print(type(2 + 3j))
    print(type("kek"))
    print(type(True))


def fract():
    try:
        fr = Fraction(input("Enter a fraction: "))
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print(fr)


def cmplx():
    try:
        cmplx = complex(input("Enter a complex number as 'a+bj'"))
    except ValueError:
        print("Enter as 'a+bj' & without spaces.")
    print(cmplx)

    # c_1 = complex(2, 3)
    # c_2 = complex(4, 6)

    # print(abs(7 + 9j))

    # print(c_1 * c_2)
    # print(c_1 / c_2)
    # print(c_1 + c_2)
    # print(c_1 - c_2)

    # print(c_1.conjugate())
    # print(c_2.conjugate())

    # print(c_1.real)
    # print(c_1.imag)

    # print(c_2.real)
    # print(c_2.imag)


def calc():
    try:
        num_1 = float(input("Enter 1st number: "))
    except ValueError:
        print("Bad input!")

    try:
        num_2 = float(input("Enter 2nd number: "))
    except ValueError:
        print("Bad input!")

    product = num_1 * num_2
    print(product)


def factor(a, b):
    if (b % a) == 0:
        # print(f"{a} is a factor of {b}")
        return a


def all_factors(x):
    i = 1
    factor_list = []
    while (i <= x):
        if isinstance(factor(i, x), int):
            factor_list.append(factor(i, x))
        i = i + 1
    # print(f"Factors of {x} are {factor_list}")
    return factor_list


# def factorStore(x):
#     for i in range(1, x+1):


def solve_quadratic(a, b, c):
    D = (b*b - 4*a*c)
    x_1 = (-b + math.sqrt(D))/(2*a)
    x_2 = (-b - math.sqrt(D))/(2*a)
    roots = (x_1, x_2)
    return(roots)


def my_range():
    for i in range(5):
        print(i)
    for i in range(1, 11):
        print(i)
    for i in range(0, 10, 3):
        print(i)


def multi_table(a):
    for i in range(1, 11):
        print(f"{a} x {i} = {a*i}")


def format(x):
    print("{0:.2f}".format(x))


def feet_to_meters(feet, inches):
    if isinstance(feet, int):
        if isinstance(inches, int):
            feet = float(feet + (inches / 12))
            return (feet * 0.3048)
        else:
            return ("Integers only!")
    else:
        return ("Integers only!")


def miles_to_kilometers(miles):
    return (miles * 1.60934)


def F_to_C(F):
    return ((F - 32) * (5/9))


def C_to_F(C):
    return ((C * (9/5)) + 32)


def C_to_K(C):
    return (C + 273.15)


def print_menu():
    print("1. feet to meters")
    print("2. miles to kilmometers")
    print("3. fahrenheit to celsius")
    print("4. celsius to fahrenheit")
    print("5. celsius to kelvin")


# def switch(n):
#     switcher = {}


if (__name__ == "__main__"):
    print_menu()
    choice = input("Enter a listed number: ")
    if choice == "1":
        feet = int(input("Enter feet (as int): "))
        inches = int(input("Enter inches (as int): "))
        print(feet_to_meters(feet, inches))
    if choice == "2":
        miles = float(input("Enter miles: "))
        print(miles_to_kilometers(miles))
