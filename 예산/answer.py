def solution(d, budget):
    count = 0
    for x in sorted(d):
        if x <= budget:
            budget -= x
            count += 1
        else:
            break
    return count