def solution(n, arr1, arr2):
    def computeBinaryNum(num):
        binary_numbers = list(map(int, bin(num)[2:]))
        if len(binary_numbers) < n:
           return [0] * (n-len(binary_numbers)) + binary_numbers
        return binary_numbers 
    toBinaryNumA = list(map(computeBinaryNum, arr1))
    toBinaryNumB = list(map(computeBinaryNum, arr2))

    wallArr = []
    for x, y in zip(toBinaryNumA, toBinaryNumB):
        tmp = []
        for a, b in zip(x, y):
          tmp.append(a+b)
        wallArr.append(tmp)
    
    result = []
    for wall in wallArr:
        wallStr = ''
        for i in range(len(wall)):
            wallStr += '#' if wall[i] else ' '
        result.append(wallStr)
    return result