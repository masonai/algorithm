

def solution(N):
    N = bin(N)[2:]

    arr_ = []
    for i in range(len(N)):
        if N[i] == '1':
            arr_.append(i)

    if len(arr_) == 1:
        return 0

    r = []
    for i in range(len(arr_)):
        if i < len(arr_)-1:
            r.append(arr_[i+1] - arr_[i])


    return max(r)-1

    pass


a = solution(1041)
print(a)