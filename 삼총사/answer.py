count = 0
def solution(number):
    cb = [0] * 3
    def DFS(L, S):
        global count
        if L == 3:
            if sum(cb) == 0:
                count = count + 1
        else:
            for i in range(S, len(number)):
                cb[L] = number[i]
                DFS(L + 1, i + 1)
        return count
    return DFS(0, 0)