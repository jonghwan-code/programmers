def solution(s):
    arr = s.split(' ')
    for i in range(len(arr)):
        tmp = list(arr[i])
        for j in range(len(tmp)):
            tmp[j] = tmp[j].lower() if j % 2 else tmp[j].upper()
        arr[i] = ''.join(tmp)
    return ' '.join(arr)