

# [3, 8, 9, 7, 6], 3


def solution(A, K):
    arr_= list(range(len(A)))
    for i in range(len(A)):
        arr_[(i+K) % len(A)] = A[i]

    return arr_
    pass

A = [3, 8, 9, 7, 6]
K = 3
r = solution(A, K)
print(r)