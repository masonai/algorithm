
def solution(A):

    A = sorted(A)
    for i in range(len(A)):
        if i+1 != A[i]:
            return i+1

    return len(A)+1

    pass


A = [2, 5, 3, 4]
r = solution(A)
print(r)