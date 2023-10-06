def solution(s):
    ref = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    result = ''
    tmp = ''
    for c in s:
        if c.isdigit():
            result += c
        else:
            tmp += c
            if tmp in ref:
                result += str(ref.index(tmp))
                tmp = ''
            else:
                continue
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

