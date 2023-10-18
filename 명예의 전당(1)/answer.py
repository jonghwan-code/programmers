def solution(k, score):
    lastSingersPt = []
    honorList = []
    for x in score:
        honorList.append(x)
        honorList.sort(reverse=True)
        lastSingersPt.append(honorList[:k][-1])

        # if len(honorList) > k:
        #     honorList = honorList[:k]
        # lastSingersPt.append(honorList[-1])
    return lastSingersPt
