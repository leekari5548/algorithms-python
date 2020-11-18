from typing import List

# https://leetcode-cn.com/problems/gas-station/
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    gas_num = 0
    temp_gas = 0
    count = len(gas)
    length = len(gas)
    start = 0
    is_start = True
    while count:
        print(f' ------------------------------------ [count = {count}] ------------------------------------')
        for index in range(length):
            temp_gas += gas[index]
            temp_gas -= cost[index]
            print(f'gas = {gas[index]}, cost = {cost[index]}, gas_size = {length}')
            if temp_gas >= 0:
                if is_start and start == 0:
                    start = index
                    is_start = False
                print(f'in fact => [gas = {gas[index]}, cost = {cost[index]}]')
                gas_num += gas[index]
                gas_num -= cost[index]
                gas.remove(gas[index])
                length -= 1
                break
            else:
                temp_gas = gas_num
        count -= 1
    print(gas_num)
    if gas_num >= 0:
        return start
    return -1


if __name__ == '__main__':
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    print(canCompleteCircuit(gas, cost))