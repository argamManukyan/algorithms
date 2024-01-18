""" O(log n) """
arr = [1, 2, 3, 4, 7, 11, 19]


def binsearch(elements: list[int], target: int) -> int:
    """Returns an index of found element"""

    left = 0
    right = len(elements) - 1

    while left <= right:
        mididx = (left + right) // 2

        if elements[mididx] < target:
            left = mididx + 1
        elif elements[mididx] > target:
            right = mididx - 1
        else:
            return mididx

    return False


if __name__ == "__main__":

    res = binsearch(arr, 11)
    print(res)
