def solution(k, m, score):
    score.sort(reverse=True)
    res = 0
    for i in range(0, len(score), m):
        tmp = score[i:i+m]
        if (len(tmp) == m):
            res += min(tmp) * len(tmp)
    return res