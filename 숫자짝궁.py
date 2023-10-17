'''
https://school.programmers.co.kr/learn/courses/30/lessons/131128
'''


def solution(X, Y):
    count_X = dict()
    matched_nums = ''
    for numX in X:
        count_X[numX] = count_X[numX] + 1 if numX in count_X else 1
    for numY in Y:
        if numY in count_X and count_X[numY] != 0:
            count_X[numY] -= 1
            matched_nums += numY

    if len(matched_nums) == 0:
        return '-1'

    if matched_nums[0] == '0':
        matched_nums = '0'

    return ''.join(sorted(matched_nums, reverse=True))
