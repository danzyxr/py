def linear_search(arr, target):
    for item in range(len(arr)):
        if arr[item] == target:
            return True
    return False


def binary_search_i(arr, target):
    lo = 0
    hi = len(arr)
    arr.sort()
    while lo <= hi:
        mid = (lo + hi) // 2
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return False


def binary_search_r(arr, target, lo, hi):
    if lo > hi:
        return False
    else:
        arr.sort()
        mid = (lo + hi) // 2
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            return binary_search_r(arr, target, lo, mid - 1)
        else:
            return binary_search_r(arr, target, mid + 1, hi)


data = [2, 4, 8, 16, 3, 6, 9, 11, -1, -3, -5]

print(binary_search_i(data, -3))

print(binary_search_r(data, 3, 0, len(data) - 1))
