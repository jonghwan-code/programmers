'''
https://school.programmers.co.kr/learn/courses/30/lessons/161989
'''

def solution(n, m, section):
    offset = section[0]
    count = 1
    for i in range(1, len(section)):
        if offset + m - 1 < section[i]:
            count += 1
            offset = section[i]
        else:
            continue
    return count