def solution(s):
    word_arr = s.split(' ')
    result = []
    for word in word_arr:
        char_arr = [char.lower() if idx % 2 else char.upper()
                    for idx, char in enumerate(list(word))]
        # for idx, char in enumerate(char_arr):
        #     char_arr[idx] = char.lower() if idx % 2 else char.upper()
        # print(char_arr)
        result.append(''.join(char_arr))
    return ' '.join(result)
