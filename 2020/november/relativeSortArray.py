from typing import List


# 暴力法
def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    if not arr1:
        return arr1
    if not arr2:
        arr1.sort()
        return arr1
    result = []
    is_continue = True
    length = len(arr1)
    count = 0
    for i in arr2:
        while is_continue:
            if count == length - 1:
                is_continue = False
            if i == arr1[count]:
                result.append(i)
                arr1.remove(i)
                count -= 1
                length -= 1
            else:
                count += 1
        is_continue = True
        count = 0
    arr1.sort()
    result.extend(arr1)
    return result


# 计数排序
def relativeSortArray_count_sort(arr1: List[int], arr2: List[int]) -> List[int]:
    upper = max(arr1)
    base_arr = [0] * (upper + 1)
    for a in arr1:
        base_arr[a] += 1

    ans = list()
    for a in arr2:
        ans.extend([a] * base_arr[a])
        base_arr[a] = 0
    for x in range(upper + 1):
        if base_arr[x] > 0:
            ans.extend([x] * base_arr[x])
    return ans


# todo 自定义排序，哈希表。。。。

if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(relativeSortArray_count_sort(arr1=arr1, arr2=arr2))
