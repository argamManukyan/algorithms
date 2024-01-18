"""Finding the missed 1 number in the array"""
from typing import Union


def findnum(elements: list[int], n: int) -> Union[int, None]:

    temp_list = [False] * (n + 1)

    for i in range(n):
        temp_list[elements[i - 1]] = True

    for element in range(1, len(temp_list)):
        if temp_list[element] is False:
            return element


if __name__ == "__main__":
    nums_list = [1, 2, 3, 4, 5, 7]
    n = len(nums_list) + 1  # missed number of digits
    result = findnum(nums_list, n)
    print(result)
    # 6