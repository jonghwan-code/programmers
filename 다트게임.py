'''
https://school.programmers.co.kr/learn/courses/30/lessons/17682
'''

import re


def solution(dartResult):
    reg = re.compile('(\d+)([SDT])([*#]?)')
    dart = reg.findall(dartResult)

    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    return sum(dart)
