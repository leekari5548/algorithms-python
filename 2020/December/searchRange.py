from typing import List

# O(n)
def searchRange(nums: List[int], target: int) -> List[int]:
    count = 0
    start = -1
    for i in range(len(nums)):
        if nums[i] == target:
            if start == -1:
                start = i
            count += 1
    if start == -1:
        return [-1, -1]
    else:
        return [start, start + count - 1]

# O(log(n))
def searchRange_log(nums: List[int], target: int) -> List[int]:
    count = 0
    start = -1

    for i in range(len(nums)):
        if nums[i] == target:
            if start == -1:
                start = i
            count += 1
    if start == -1:
        return [-1, -1]
    else:
        return [start, start + count - 1]

def binarySearch(nums: List[int], target: int, start: int, end: int) -> int:
    lower = start
    higher = end - 1
    while lower <= higher:
        mid = (higher - lower) // 2
        midVal = nums[mid]
        if midVal > target:
            higher = mid - 1
        elif midVal < target:
            lower = mid + 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(binarySearch(nums, target, 0, len(nums)))
    # print(searchRange(nums, target))
