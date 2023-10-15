def solution(numbers):
    cb = [0] * 2
    res = []
    def DFS(L, S):
        if L == 2:
            res.append(sum(cb))
        else:
            for i in range(S, len(numbers)):
                cb[L] = numbers[i]
                DFS(L + 1, i + 1)
        return sorted(list(set(res)))
    return DFS(0, 0)