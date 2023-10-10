'''
https://school.programmers.co.kr/learn/courses/30/lessons/12921
'''

def isPrime(num):
    if num < 2:
        return True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    else:
        return True
        
def solution(n):
    count = 0
    for i in range(2, n+1):
        if isPrime(i):
            count += 1
    return count