def test(tester, answers):
    t, k = divmod(len(answers), len(tester))
    return [True if a == b else False for a, b in zip(tester*t + tester[:k], answers)]
    
def solution(answers):
    oneP = test([1, 2, 3, 4, 5], answers).count(True)
    twoP = test([2, 1, 2, 3, 2, 4, 2, 5], answers).count(True)
    thiP = test([3, 3, 1, 1, 2, 2, 4, 4, 5, 5], answers).count(True)
    tmp = [oneP, twoP, thiP]
    mx = max(tmp)
    res = []
    for idx, val in enumerate(tmp):
        print(idx, val, mx)
        if val == mx:
            res.append(idx+1)
    return res