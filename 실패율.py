'''
https://school.programmers.co.kr/learn/courses/30/lessons/42889
'''

def solution(N, stages):
    totalUser = len(stages)
    result = []
    for i in range(1, N+1):
        if i in stages:
            curCount = stages.count(i)
            result.append([i, curCount / totalUser])
            totalUser = totalUser - curCount
        else:
            result.append([i, 0])
    result.sort(key=lambda x: x[1], reverse=True)
    return list(map(lambda x: x[0] , result))