def info():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    salary = float(input("Enter your salary: "))
    return fname, lname, salary


def new_salary(salary):
    if salary < 40000:
        new_salary = (salary * 0.05) + salary
    else:
        salary = 2000 + (salary * 0.02) + salary
    return new_salary


def display(f_n, l_n, s):
    print(f"{f_n} {l_n}'s new salary is {s}")


def main():
    fn, ln, sal = info()
    sal = new_salary(sal)
    display(fn, ln, sal)


main()
