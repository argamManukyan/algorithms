arr = [1, 22, -9, 99, 14, 89, -5]


def quick_sort(elements: list):

    if len(elements) < 2:
        return elements

    pivot = elements[0]
    less_nums = [i for i in elements[1:] if i < pivot]
    greater_nums = [i for i in elements[1:] if i > pivot]

    return quick_sort(less_nums) + [pivot] + quick_sort(greater_nums)


if __name__ == "__main__":
    res = quick_sort(arr)
    print(res)