def starting(s):
    result = []
    result1 = []
    perumteStr(result, "",s )
    subsetsStr(result1,"",s,0)
    print(result,result1)
    pass


def perumteStr(result,temp,s):
    if len(temp) == len(s):
        result.append(temp)
    else:
        for i in range(len(s)):
            if s[i] in temp:
                continue
            temp += s[i]
            perumteStr(result,temp,s)
            temp = temp[:-1]

def subsetsStr(result,temp,s,ind):
    if len(temp) >=0:
        if temp not in result:
            result.append(temp)
    for i in range(ind,len(s)):
        if s[i] in temp:
            continue
        temp += s[i]
        subsetsStr(result,temp,s,i+1)
        temp = temp[:-1]

starting('aac')