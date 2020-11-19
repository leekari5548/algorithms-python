from typing import List

# https://leetcode-cn.com/problems/move-zeroes/submissions/
def moveZeroes(nums: List[int]) -> None:
    index, count, zero_count = 0, len(nums), 0
    while count:
        if nums[index] == 0:
            nums.remove(0)
            zero_count += 1
        else:
            index += 1
        count -= 1
    nums.extend([0] * zero_count)


def moveZeroes1(nums: List[int]) -> None:
    i = 0
    for index in range(len(nums)):
        if nums[index] != 0:
            nums[i] = nums[index]
            i += 1
    for index in range(i, len(nums)):
        nums[index] = 0


if __name__ == '__main__':
    var = [0, 1, 0, 3, 12]
    moveZeroes1(var)
    print(var)
