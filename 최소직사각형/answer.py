def solution(sizes):
    bigX, bigY = [-2147000000] * 2
    for x in sizes:
        if x[1] > x[0]:
            x[0], x[1] = x[1], x[0]
        bigX = max(x[0], bigX)
        bigY = max(x[1], bigY)
    return bigX * bigY