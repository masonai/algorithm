
def solution(X, A):
    l = [0] * X
    l_sum = 0
    for i in range(len(A)):
        tmp = A[i] - 1
        if l[tmp] == 0:
            l_sum += 1
        l[tmp] = 1

        if l_sum == X:
            return i

    return -1

    pass


X = 5
A = [1,3,1,4,2,3,5,4]

a = solution(X, A)
print(a)