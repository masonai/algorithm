
def solution(N, A):
    arr_ = [0] * N

    max_c = 0
    for i in range(len(A)):
        idx = A[i] - 1

        if idx == N:
#            current_max = max(arr_)
            arr_ = [max_c] * N
            continue

        arr_[idx] += 1
        max_c = max(arr_[idx], max_c)

    return arr_
    pass


N = 5
#A = [3,4,4,6,1,4,4]
#A = [1,1,2,6,6]
A = [1,2,3,4,1,6]

a = solution(N, A)
print(a)