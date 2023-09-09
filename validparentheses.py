def isValid(s: str) -> bool:
    d = {'(':')', '{':'}','[':']'}
    m = []

    for x in s:
        if x in d:
            m.append(x)

        else: 
            if len(m) and d[m[-1]] == x:
                del m[-1]
            else:
                return False

    return not m


def isValid2(s: str) -> bool:
    c = 0
    for x in s:
        if x in '([{': 
            c += 1
        if x in ')]}':
            c -= 1
        if c < 0:
            return False
    return True if c == 0 else False

x = isValid2('[](){}')
print(x)