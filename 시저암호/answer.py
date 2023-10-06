def check(c, number):
    if 97 <= ord(c) <= 122 and 122 < ord(c) + number:
        return chr(97 +(ord(c) + number - 123))
    if 65 <= ord(c) <= 90 and 90 < ord(c) + number:
        return chr(65 + (ord(c) + number - 91))
    else:
        return chr(ord(c) + number)
def solution(s, n):
    res = ''
    for x in s:
        if x == ' ':
            res += ' '
        else:
            res += check(x, n)
    return res