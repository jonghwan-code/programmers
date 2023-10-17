def solution(n, lost, reserve):
    stduent_gymsuit = [1]*n
    for x in range(n):
        if x + 1 in lost:
            stduent_gymsuit[x] -= 1
        if x + 1 in reserve:
            stduent_gymsuit[x] += 1

    for idx, val in enumerate(stduent_gymsuit):
        if val == 0:
            if 0 <= idx - 1 and stduent_gymsuit[idx - 1] > 1:
                stduent_gymsuit[idx - 1] -= 1
                stduent_gymsuit[idx] += 1
            elif idx + 1 < n and stduent_gymsuit[idx + 1] > 1:
                stduent_gymsuit[idx + 1] -= 1
                stduent_gymsuit[idx] += 1

    return len(list(filter(lambda x: x > 0, stduent_gymsuit)))
