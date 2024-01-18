"""Find the sum of numbers which will be equal to the target number O(n)"""


def find_two_sum(num_list: list[int], target: int):

    left = 0
    right = len(num_list) - 1

    while left < right:
        while left < right and num_list[left] + num_list[right] > target:
            right -= 1

        while left < right and num_list[left] + num_list[right] < target:
            left += 1

        if num_list[left] + num_list[right] == target:
            return [num_list[left], num_list[right]]

    return False


if __name__ == "__main__":
    target = 18
    nums = [1, 2, 8, 10, 11]
    res = find_two_sum(nums, target)
    print(res)
