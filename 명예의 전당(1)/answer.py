def solution(k, score):
    res = []
    tmp = []
    for x in score:
        tmp.append(x)
        tmp.sort(reverse=True)
        if len(tmp) > k:
            tmp.pop()
        res.append(tmp[-1])
    return res