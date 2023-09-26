def solution(number):
    cb = [0] * 3
    res = []
    def DFS(L, S):
        if L == 3:
            if sum(cb) == 0:
                res.append(1)
        else:
            for i in range(S, len(number)):
                cb[L] = number[i]
                DFS(L + 1, i + 1)
    DFS(0, 0)
    return len(res)