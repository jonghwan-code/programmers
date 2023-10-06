def solution(n):
    ternary = ''
    while n > 0:
        n, k = divmod(n, 3)
        ternary += str(k)
    return int(ternary, 3)