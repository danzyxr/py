"""
Generators,
List Comprehension,
and Other Stuff
"""


def squared(nums):
    for n in nums:
        yield n ** 2


def coord_adder(x, y, z, n):
    return list(
        [
            [i, j, k]
            for i in range(x + 1)
            for j in range(y + 1)
            for k in range(z + 1)
            if ((i + j + k) == n)
        ]
    )


def runner_up():
    arr = map(int, input().split())
    arr = sorted(list(set(arr)))
    print(arr[-2])


runner_up()


if __name__ == "__main__":
    my_arr = [1, 2, 3, 4, 5, 6]

    print(list(squared(my_arr)))
    print([n * n * n for n in my_arr])

    print(coord_adder(2, 4, 6, 6))

    print(list(map(lambda n: n * 3, my_arr)))

    print(list(filter(lambda n: n % 2 == 0, my_arr)))
    print([n for n in my_arr if n % 2 == 0])

    real_name = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
    hero_name = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]
    print(list(zip(real_name, hero_name)))

    my_heroes = {}
    for real, hero in zip(real_name, hero_name):
        my_heroes[real] = hero
    print(my_heroes)
