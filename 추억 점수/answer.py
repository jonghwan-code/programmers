def solution(name, yearning, photo):
    def find_friend(x):
        t = set(x) & set(name)
        return list(t)
    friends_in_photos = list(map(find_friend, photo))
    res = []
    for friends in friends_in_photos:
        point = []
        for friend in friends:
            idx = name.index(friend)
            point.append(yearning[idx])
        res.append(sum(point))
    return res