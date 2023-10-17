'''
https://school.programmers.co.kr/learn/courses/30/lessons/133499
'''


def solution(babbling):
    speakable = ["aya", "ye", "woo", "ma"]
    count = 0
    for word in babbling:
        for s in speakable:
            if s * 2 not in word:
                word = word.replace(s, ' ')
        if word.strip() == '':
            count += 1
    return count
