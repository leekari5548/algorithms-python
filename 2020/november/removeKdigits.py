# 失败1
def removeKdigits(num: str, k: int) -> str:
    num_list = list(num)
    ans = list()
    length = len(num_list) - k
    while length > 0:
        if k == 0:
            ans.extend(num_list)
            break
        lower = 9
        lower_index = 0
        for index in range(length):
            temp = min(int(num_list[index]), lower)
            if temp != lower:
                lower = temp
                lower_index = index
        num_list = num_list[(lower_index + 1):]
        ans.append(lower)
        print(f'lower_index = {lower_index}, lower = {lower}, num_list = {num_list}, ans = {ans}, length = {length}')
        length -= 1
        k -= 1

    return parseAns(num_list)

def parseAns(numList):
    result = ''
    for number in numList:
        result += str(number)
    result = result.lstrip('0') if result.lstrip('0') != '' else '0'
    return result

# 失败2
def removeKdigits2(num: str, k: int) -> str:
    if k == len(num):
        return '0'
    numList = list(num)
    while k > 0:
        for i in range(len(numList)):
            if int(numList[0]) > int(numList[1]):
                numList.remove(numList[0])
            else:
                numList.remove(numList[1])
        k -= 1

    return parseAns(numList)


def removeKdigits3(num: str, k: int) -> str:
    numStack = []
    for n in num:
        while k and numStack and numStack[-1] > n:
            numStack.pop()
            k -= 1
        numStack.append(n)

    # 如果k不等于0，则截取最后的k个字符
    finalStack = numStack[:-k] if k else numStack
    # string.join(seq)	使用字符串连接序列的每一个元素组成一个新的字符串
    return "".join(finalStack).lstrip('0') or '0'


if __name__ == '__main__':
    num = "112"
    k = 1
    print(removeKdigits3(num, k))
