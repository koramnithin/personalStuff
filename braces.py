def braces(values):
    res = []
    for j in values:
        s = []
        for i in j:
            if i == '{' or i == '[' or i == '(':
                s.append(i)
            elif i == '}':
                if s[-1] == '{':
                    s.pop()
            elif i == ']':
                if s[-1] == '[':
                    s.pop()
            elif i == ')':
                if s[-1] == '(':
                    s.pop()
        if len(s) != 0:
            res.append('NO')
        else:
            res.append('YES')

    return res

print(braces(['{}','[[]]']))