def solution(s, n):
    res = ''
    for x in s:
        if x == ' ':
            res += x
        else:
            stdChar = 'A' if 'A' <= x <= 'Z' else 'a'
            res += chr((ord(x) - ord(stdChar) + n) % 26 + ord(stdChar))
    return res