def solution(s):
    word_arr = s.split(' ')
    result =[]
    for word in word_arr:
        char_arr = list(word)
        for idx, char in enumerate(char_arr):
            char_arr[idx] = char.lower() if idx % 2 else char.upper()
        result.append(''.join(char_arr))
    return ' '.join(result)