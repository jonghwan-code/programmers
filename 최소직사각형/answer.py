def solution(sizes):
    bigX, bigY = [-2147000000] * 2
    for x in sizes:
        if x[1] > x[0]:
            x[0], x[1] = x[1], x[0]
    for x in sizes:
        if x[0] > bigX:
            bigX = x[0]
        if x[1] > bigY:
            bigY = x[1]
    return bigX * bigY