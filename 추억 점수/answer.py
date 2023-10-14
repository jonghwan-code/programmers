def solution(name, yearning, photo):
    def find_friend(x):
        t = set(x) & set(name)
        return list(t)
    friends_list = list(map(find_friend, photo))
    res = []
    for friends in friends_list:
        point = []
        for friend in friends:
            idx = name.index(friend)
            point.append(yearning[idx])
        res.append(sum(point))
    return res

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]	))