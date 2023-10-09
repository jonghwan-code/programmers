def solution(nums):
    setLen = len(list(set(nums)))
    maxPoc = len(nums) // 2
    return min(setLen, maxPoc)