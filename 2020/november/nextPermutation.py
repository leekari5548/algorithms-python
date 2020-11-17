from typing import List


def nextPermutation(nums: List[int]) -> None:
    if len(nums) == 1:
        return
    nums_reverse = nums[::-1]
    if nums.sort() == nums_reverse:
        nums_reverse.sort()
        for i in range(len(nums)):
            nums[i] = nums_reverse[i]
    else:
        max_value = 0
        max_index = 0
        for i in range(len(nums)):
            max_temp = max(nums[i], max_value)
            if max_temp == nums[i]:
                max_value = max_temp
                max_index = i


if __name__ == '__main__':
    l = [3, 2, 1]
    nextPermutation(l)
    print(l)
