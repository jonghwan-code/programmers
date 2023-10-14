def solution(s):
    word_arr = s.split(' ')
    result =[]
    for word in word_arr:
        char_arr = list(word)
        for i in range(len(char_arr)):
            char_arr[i] = char_arr[i].lower() if i % 2 else char_arr[i].upper()
        result.append(''.join(char_arr))
    return ' '.join(result)