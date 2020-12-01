def reorganizeString(S: str) -> str:
    ls = list(S)
    length = len(ls)
    res = []
    while length and ls:
        if not res:
            res.append(ls[0])
        else:
            temp = 0
            l = len(ls)
            # while l:

            for data in ls:
                temp += 1
                if res[len(res) - 1] != data:
                    res.append(data)
                    ls.remove(data)
                print(f'temp = {temp}, len(res) = {len(ls)}, res = {temp == len(ls)}')
            if temp == len(ls) and ls[0] == res[len(res) - 1]:
                return ""
        length -= 1
    return "".join(res)


if __name__ == '__main__':
    print(reorganizeString('aab'))
