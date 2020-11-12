from typing import List


# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000

def sortArrayByParityII(A: List[int]) -> List[int]:
    even, odd = 0, 1
    result = [0] * len(A)
    for item in A:
        print(f'item {item} % 2 = {item % 2}')
        if item % 2 == 0:
            print(f'even = {even} && item = {item}')
            result[even] = item
            even += 2
        else:
            print(f'odd = {odd} && item = {item}')
            result[odd] = item
            odd += 2
    return result


if __name__ == '__main__':
    l = [1,2,3,4]
    print(sortArrayByParityII(l))
