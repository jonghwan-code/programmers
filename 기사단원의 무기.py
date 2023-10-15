'''
https://school.programmers.co.kr/learn/courses/30/lessons/136798
'''

def countDivisor(n, limit, power):
    divisorsList = []
    for i in range(1, int(n**0.5) + 1):
        if (n % i == 0):
            divisorsList.append(i)
            if (i**2) != n: 
                divisorsList.append(n // i)
    if len(divisorsList) > limit:
        return power
    else:
        return len(divisorsList)
    
def solution(number, limit, power):
    divisors = []
    for i in range(1, number+1):
        divisors.append(countDivisor(i, limit, power))
    return sum(divisors)