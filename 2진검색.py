from typing import Any, Sequence


def bin_search(a: Sequence, key: Any) -> int:

    left = 0
    right = len(a) - 1

    while True:
        center = (left + right) // 2

        if a[center] == key:
            return center

        elif a[center] < key:
            left = center + 1

        else:
            right = center - 1

        if left > right:
            break
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 9, 10]


print(bin_search(arr, 1))
