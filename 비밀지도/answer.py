def solution(n, arr1, arr2):
    def computeBinaryNum(num):
      binaryNum = bin(num)[2:]
      return int(binaryNum)
    
    def makeFiveLength(binarySum):
        if len(binarySum) < n:
          return '0' * (n-len(binarySum)) + binarySum
        return binarySum
    
    toBinaryNumA = list(map(computeBinaryNum, arr1))
    toBinaryNumB = list(map(computeBinaryNum, arr2))

    wallArr = [makeFiveLength(str(x + y)) for x, y in zip(toBinaryNumA, toBinaryNumB)]
    res= []
    for wall in wallArr:
        number = wall
        for code in wall:
            if int(code) >= 1:
                number = number.replace(code, '#')
            else:
                number = number.replace(code, ' ')
        res.append(number)
    return res         
print(solution(5, [2, 20, 28, 18, 11], [1, 1, 21, 17, 28]))
