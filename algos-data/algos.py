import string

'''
So this might be useful...
Data Structures and Algorithms!!
1:        constant
log(n):   logarithmic
n:        linear
nlog(n):  log linear
n^2:      quadratic
n^3:      cubic
2^n:      exponential
There are more!
'''


def total(n):
    total = 0  # O(n + 1)
    for x in range(n + 1):
        total += x
    return total


def sum_formula(n):
    return (n*(n + 1))/2


def reverseArray(arr):
    # return arr[::-1]
    # return reversed(arr)
    arr.reverse()
    return arr


def anagram_v1(str_1, str_2):
    str_1 = str_1.replace(' ', '').lower()
    str_2 = str_2.replace(' ', '').lower()
    return sorted(str_1) == sorted(str_2)


def count_chars(s, d):  # str, dict
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d


def anagram_v2(str_1, str_2):
    str_1 = str_1.replace(' ', '').lower()
    str_2 = str_2.replace(' ', '').lower()

    if len(str_1) != len(str_2):
        return False

    letters_1 = {}
    letters_2 = {}
    # count the number of each char
    letters_1 = count_chars(str_1, letters_1)
    letters_2 = count_chars(str_2, letters_2)
    print(f"{str_1}: {letters_1}")
    print(f"{str_2}: {letters_2}")
    return True if letters_1 == letters_2 else False


def pair_sum(arr, k):
    known = set()
    pairs = set()

    if len(arr) < 2:
        return ("Too small!")

    for n in arr:
        diff = k - n
        if diff not in known:
            known.add(n)
        else:
            pairs.add((min(n, diff), max(n, diff)))

    if pairs == set():
        return ("No know pairs!")
    else:
        return pairs


def reverse_str_v1(s):
    return " ".join(reversed(s.split()))


def reverse_str_v2(s):
    i = 0
    words = []
    while i < len(s):
        if s[i] != " ":
            word_start = i
            while i < len(s) and s[i] != " ":
                i += 1
            words.append(s[word_start:i])
        i += 1
    return " ".join(reversed(words))


def unique_chars(s):
    s = s.lower()
    return len(s) == len(set(s))


def is_palindrome_v1(s):
    s = s.replace(" ", "").lower()
    del_punct = str.maketrans('', '', string.punctuation)
    s = s.translate(del_punct)
    return s == s[::-1]


def is_palindrome_v2(s):
    i = 0
    j = len(s) - 1

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1

    return True


def two_sum(arr, k):
    diffs = {}
    if len(arr) < 2:
        return "Too small!"
    for n in range(len(arr)):
        if arr[n] in diffs:
            return [diffs[arr[n]], n]
        else:
            diffs[k - arr[n]] = n
    return "No match!"


def one_occurance(arr):
    counted = {}
    for n in range(len(arr)):
        if arr[n] in counted:
            counted[arr[n]] += 1
        else:
            counted[arr[n]] = 1
    for n, count in counted.items():
        if count == 1:
            return n


def fizz_buzz(n):
    i = 1
    while i <= n:
        if ((i % 3 == 0) and (i % 5 != 0)):
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("FizzBuzz")
        else:
            print(i)
        i += 1


def factorial_i(n):
    x = 1
    for i in range(n, 0, -1):
        x = x * i
    return x


def factorial_r(n):
    if (n <= 1):
        return 1
    else:
        return n * factorial_r(n - 1)


def find_uppercase(s):
    uc = []
    for i in range(len(s)):
        if s[i].isupper():
            uc.append(s[i])
    return uc


def median_matrix(A):
    if len(A) == 1:
        vec = A[0]
        return vec[len(vec) // 2]
    else:
        new_list = []
        for row in range(len(A)):
            new_list.extend(A[row])
        new_list.sort()
    return new_list[len(new_list) // 2]


def compress_string(s):
    cs = ""
    count = 1

    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            cs = cs + (str(s[i] + str(count)))
            count = 1
            continue
        if s[i] == s[i + 1]:
            count += 1
    cs += s[i] + str(count)
    if len(cs) <= len(s):
        return cs
    else:
        return s


if __name__ == "__main__":
    x = 5
    print(total(x))
    print(sum_formula(x))

    my_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
    arrggh = [7, -7, 13, -13, 23, -23, 3, -3, 0]

    print(my_arr)
    print(reverseArray(my_arr))

    print("\nanagram_v1")
    print(anagram_v1('god', 'dog'))
    print(anagram_v1('mom', 'dad'))

    print("\nanagram_v2")
    print(anagram_v2('god', 'dog'))
    print(anagram_v2('mom', 'dad'))

    print("\npair_sum:")
    print(pair_sum(my_arr, 10))
    print(pair_sum(arrggh, 10))

    print("\nreverse_str:")
    print(reverse_str_v1("This is the best!"))
    print(reverse_str_v2("This is the best!"))

    print("\nunique_chars:")
    print(unique_chars("Daniel"))
    print(unique_chars("Unique"))

    print("\nis_palindrome v1:")
    print(is_palindrome_v1("Hannah"))
    print(is_palindrome_v1("Dammit I'm mad!"))
    print(is_palindrome_v1("Racecar"))

    print("\nis_palindrome v2:")
    print(is_palindrome_v1("Hannah"))
    print(is_palindrome_v1("Dammit I'm mad!"))
    print(is_palindrome_v1("Racecar"))

    print("\ntwo_sum:")
    a = [1, 3, 11, 2, 7]
    print(two_sum(a, 9))

    print("\none_occurance:")
    arr = [1, 1, 6, 6, 3, 3, 7]
    print(one_occurance(arr))

    print("\nfizz_buzz:")
    fizz_buzz(25)

    print("\nfactorial_i:")
    print(factorial_i(5))
    print("\nfactorial_r:")
    print(factorial_r(5))

    print("\nfind_uppercase:")
    print(find_uppercase("Your mom!"))
    print(find_uppercase("sPOnGEbOB"))

    l3 = [9, 1, 6]
    l2 = [3, 5, 7]
    l1 = [2, 4, 8]

    matrix = [l1, l2, l3]
    print("\nmedian_matrix:")
    print(median_matrix(matrix))

    print("\ncompress_string:")
    print(compress_string("abbcccdddd"))
    print(compress_string("asdfqwerty"))
