def solution(n, arr1, arr2):
    a = [int(bin(x).replace('0b', '')) for x in arr1]
    b = [int(bin(x).replace('0b', '')) for x in arr2]
    tmp = [str(x + y) for x, y in zip(a, b)]
    res = []
    for i in range(n):
        if len(tmp[i]) < n:
            tmp[i] = ('0' * (n-len(tmp[i]))) + tmp[i]
        number = tmp[i]
        for q in tmp[i]:
            if int(q) >= 1:
                number = number.replace(q, '#')
            else:
                number = number.replace(q, ' ')
        res.append(number)
    return res