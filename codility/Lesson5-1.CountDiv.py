
def solution(A, B, K):

    if K == 1:
        return B-A+1

    c = 0
    for i in range(A, B+1):
        if i % K == 0:
            c+=1
    return c
    pass


A = 0
B = 100
K = 1

a = solution(A, B, K)

print(a)