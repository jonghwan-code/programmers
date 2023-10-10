'''

'''


def isPrime(num):
    if num < 2:
        return True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    else:
        return True
        
def solution(nums):
    cb = [0] * 3
    count = 0
    def DFS(L, S):
        nonlocal count
        if L == 3:
            if isPrime(sum(cb)):
                count += 1
        else:
            for i in range(S, len(nums)):
                cb[L] = nums[i]
                DFS(L+1, i+1)
    DFS(0, 0)
    return count