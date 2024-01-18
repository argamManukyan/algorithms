"""O (n)"""


def find_container_with_most_water(elements: list[int]) -> int:
    result = 0
    left = 0
    right = len(elements) - 1

    while left < right:
        area = (right - left) * min(elements[left], elements[right])
        result = max(result, area)

        if elements[left] < elements[right]:
            left += 1
        else:
            right -= 1

    return result


if __name__ == "__main__":
    nums = [1, 8, 6,2, 5, 4, 8, 3, 7]
    res = find_container_with_most_water(nums)
    print(res)