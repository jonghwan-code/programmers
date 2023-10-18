def test(tester, answers):
    t, k = divmod(len(answers), len(tester))
    return [a == b for a, b in zip(tester*t + tester[:k], answers)]


def solution(answers):
    oneP = test([1, 2, 3, 4, 5], answers).count(True)
    twoP = test([2, 1, 2, 3, 2, 4, 2, 5], answers).count(True)
    thiP = test([3, 3, 1, 1, 2, 2, 4, 4, 5, 5], answers).count(True)
    student_grade = [(1, oneP), (2, twoP), (3, thiP)]
    mx = max([p for s, p in student_grade])
    return [s for s, p in [(s, p) for s, p in student_grade if p == mx]]
