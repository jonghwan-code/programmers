def solution(name, yearning, photo):
    def some_fun(x):
        t = set(x) & set(name)
        return list(t)
    tmp = list(map(some_fun, photo))
    res = []
    for x in tmp:
        point = 0 
        for i in range(len(x)):
            idx = name.index(x[i])
            point += yearning[idx]
        res.append(point)
    return res