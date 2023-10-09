def solution(a, b, n):
    res = 0
    while n>=a:
        t, k = divmod(n, a)
        res = res + t*b
        n = (t*b)+k
    return res