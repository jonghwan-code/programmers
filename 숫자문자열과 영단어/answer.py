from collections import deque
def solution(s):
    ref = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    result = ''
    stringChr = ''
    s = deque(s)
    while s:
        char = s.popleft()
        stringChr += char
        if stringChr in ref:
            result += str(ref.index(stringChr))
            stringChr = ''
        elif stringChr.isdigit():
            result += char
            stringChr = ''
    return int(result)
# 다른 풀이
'''
def solution(s):
    ref = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = s
    for idx, value in enumerate(ref):
        answer = answer.replace(value, str(idx))
    return int(answer)
'''