def solution(array, commands):
    def add_one(x):
        i, j, k = x
        tmp = sorted(array[i-1:j])
        return tmp[k-1]
    return list(map(add_one, commands))