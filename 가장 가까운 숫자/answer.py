def solution(s):
    res = []
    for i in range(len(s)):
        tmp = s[:i]
        if tmp.rfind(s[i]) < 0:
            res.append(-1)
        else:
            res.append(len(tmp) - tmp.rfind(s[i]))
    return res