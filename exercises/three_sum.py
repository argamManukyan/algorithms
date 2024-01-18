"""Find the sum of numbers which will be equal to 0"""
from typing import Union


def tree_sum_nums(nums: list[int]) -> Union[list[list[int]], None]:
    res = []

    nums.sort()  # this is important case to have a sorted array

    for idx, item in enumerate(nums):
        if idx > 0 and item == nums[idx - 1]:
            continue

        left = idx + 1
        right = len(nums) - 1

        while left < right:
            sum_of_elements = item + nums[left] + nums[right]

            if sum_of_elements < 0:
                left += 1
            elif sum_of_elements > 0:
                right -= 1
            else:
                res.append([item, nums[left], nums[right]])
                left += 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    return res


if __name__ == "__main__":
    nums_list = [-1, 1, 2, 0, -2, 4, 7, -3]
    result = tree_sum_nums(nums_list)
    print(result)
    # [[-3, -1, 4], [-3, 1, 2], [-2, 0, 2], [-1, 0, 1]]
