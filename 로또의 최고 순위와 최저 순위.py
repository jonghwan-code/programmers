'''
https://school.programmers.co.kr/learn/courses/30/lessons/77484
'''


def solution(lottos, win_nums):
    count = 0
    for num in win_nums:
        count += lottos.count(num)
    min = 1 if count <= 1 else count
    max = 1 if count + lottos.count(0) == 0 else count + lottos.count(0)
    return [7 - max, 7 - min]
