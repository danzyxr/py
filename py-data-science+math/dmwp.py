# import math
from fractions import Fraction


def add(a, b):
    s = a + b
    return s


def subtract(a, b):
    d = a - b
    return d


def multiply(a, b):
    p = a * b
    return p


def divide(a, b):
    q = a / b
    return q


def get_fraction():
    try:
        fr = Fraction(input("Enter a fraction: "))
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    return fr


def cmplx():
    try:
        cmplx = complex(input("Enter a complex number as 'a+bj'"))
    except ValueError:
        print("Enter as 'a+bj' (without spaces).")
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


def get_nums():
    try:
        num_1 = float(input("Enter 1st number: "))
    except ValueError:
        print("Bad input!")
    try:
        num_2 = float(input("Enter 2nd number: "))
    except ValueError:
        print("Bad input!")
    return num_1, num_2


def my_range():
    for i in range(5):
        print(i)
    for i in range(1, 11):
        print(i)
    for i in range(0, 10, 3):
        print(i)


def custom_format(x):
    print("{0:.2f}".format(x))


def feet_to_meters(feet, inches):
    if isinstance(feet, int):
        if isinstance(inches, int):
            feet = float(feet + (inches / 12))
            return feet * 0.3048
        else:
            return "Integers only!"
    else:
        return "Integers only!"


def miles_to_kilometers(miles):
    return miles * 1.60934


def F_to_C(F):
    return (F - 32) * (5 / 9)


def C_to_F(C):
    return (C * (9 / 5)) + 32


def C_to_K(C):
    return C + 273.15


def unit_menu():
    print("0. exit")
    print("1. feet to meters")
    print("2. miles to kilmometers")
    print("3. fahrenheit to celsius")
    print("4. celsius to fahrenheit")
    print("5. celsius to kelvin")


def unit_converter():  # This is too clunky
    while True:
        unit_menu()
        choice = input("Enter a listed number: ")
        if choice == "0":
            break
        if choice == "1":
            feet = int(input("Enter feet (as int): "))
            inches = int(input("Enter inches (as int): "))
            print(str(feet_to_meters(feet, inches)) + " meters")
        if choice == "2":
            miles = float(input("Enter miles: "))
            print(str(miles_to_kilometers(miles)) + " kilometers")
        if choice == "3":
            fahrenheit = float(input("Enter degrees in fahrenheit: "))
            print(str(F_to_C(fahrenheit)) + " degrees celsius")
        if choice == "4":
            celsius = float(input("Enter degrees in celsius: "))
            print(str(C_to_F(celsius)) + " degrees fahrenheit")
        if choice == "5":
            celsius = float(input("Enter degrees in celsius: "))
            print(str(C_to_K(celsius)) + " degrees kelvin")
        input("Press enter to continue...")


# def switch(n):
#     switcher = {
#         1:
#         2:
#         3:
#     }
#     print switcher.get(n, "Invalid option")


def odd_even_vendor(x):
    if isinstance(x, int):
        vend = [x]
        for i in range(1, 10):
            vend.append(x + (2 * i))
        if (x % 2) == 0:
            print("Even")
        else:
            print("Odd")
        print(vend)
    else:
        print("Not an integer!")


def multi_table(a, b):
    for i in range(1, b + 1):
        print(f"{a} x {i} = {a*i}")


if __name__ == "__main__":
    multi_table(3, 6)
    odd_even_vendor(3)
    unit_converter()
