def solution(s):
    arr = s.split(' ')
    for i in range(len(arr)):
        tmp = list(arr[i])
        for j in range(len(tmp)):
            if j % 2:
                tmp[j] = tmp[j].lower()
            else:
                tmp[j] = tmp[j].upper()
        arr[i] = ''.join(tmp)
    return ' '.join(arr)