from stack import Stack


def is_match(a, b):
    if a == "(" and b == ")":
        return True
    if a == "[" and b == "]":
        return True
    if a == "{" and b == "}":
        return True
    else:
        return False


'''
is_balanced() will return true
for strings similar to "([{}])"
'''


def is_balanced(parens):
    s = Stack()
    is_balanced = True
    i = 0

    while (i < len(parens) and is_balanced):
        p = parens[i]
        if p in "([{":
            s.push(p)
        elif s.is_empty():
            is_balanced = False
        elif not is_match(s.pop(), p):
            is_balanced = False
        i += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


def get_binary(dec):
    s = Stack()

    while (dec > 0):
        r = dec % 2
        s.push(r)
        dec = dec // 2

    binary = ""  # dec to bin
    while not s.is_empty():
        binary += str(s.pop())
    return binary


if __name__ == "__main__":
    s = Stack()

    s.push("Tau")
    s.push("Zetta")
    s.push("Phi")

    print(s.peek())
    print(s.get_stack())
    s.pop()
    print(s.get_stack())
    s.pop()
    print(s.get_stack())
    s.pop()
    print(s.is_empty())

    print(is_balanced("[]"))
    print(is_balanced("(((("))
    print(is_balanced("[{()}]"))

    print(get_binary(1993))
