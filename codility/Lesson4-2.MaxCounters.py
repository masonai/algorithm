
def solution(N, A):
    arr_ = [0] * N

    for i in A:
        if i == N+1:
            max_c = max(arr_)
            for j in range(N):
                arr_[j] = max_c
            continue

        arr_[i-1] += 1

    return arr_
    pass


N = 5
A = [3,4,4,6,1,4,4]
#A = [1,1,2,4]

a = solution(N, A)
print(a)