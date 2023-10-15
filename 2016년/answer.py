def solution(a, b):
    counts = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    totalD = sum(counts[:a-1]) + b
    return days[totalD % 7 - 3]