from typing import List

# 来源：https://leetcode-cn.com/problems/matrix-cells-in-distance-order/
def allCellsDistOrder(R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    distance_dict = {}
    for i in range(0, R):
        distance_x = abs(i - r0)
        for j in range(0, C):
            distance_y = abs(j - c0)
            distance = distance_x + distance_y
            if distance_dict.get(distance) is None:
                distance_dict.update({distance: [[i, j]]})
            else:
                distance_dict.get(distance).append([i, j])

    key_list = list(distance_dict.keys())
    key_list.sort()
    ans = []
    for key in key_list:
        if distance_dict.get(key) is not None:
            ans.extend(distance_dict.get(key))
    return ans


if __name__ == '__main__':
    print(allCellsDistOrder(2, 3, 1, 2))
