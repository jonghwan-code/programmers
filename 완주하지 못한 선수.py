'''
https://school.programmers.co.kr/learn/courses/30/lessons/42576
'''


def solution(participant, completion):
    dictPart = dict()
    answer = ''
    for part in participant:
        if part in dictPart:
            dictPart[part] += 1
        else:
            dictPart[part] = 1

    for comPlayer in completion:
        dictPart[comPlayer] -= 1

    for player in dictPart:
        if dictPart[player] > 0:
            answer += player
    return answer
