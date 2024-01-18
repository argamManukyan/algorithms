""" O(log n * n) """

arr = [1, 22, -9, 99, 14, 89, -5, -7]


def findmin(elements: list[int]) -> int:
    small_idx = 0
    small_val = elements[0]

    for idx in range(1, len(elements)):
        if elements[idx] < small_val:
            small_idx = idx
            small_val = elements[idx]

    return small_idx


def selection_sort(elements: list[int]):
    res = []

    for element in range(len(elements)):
        res.append(elements.pop(findmin(elements)))

    return res


if __name__ == "__main__":
    res = selection_sort(arr)
    print(res)
