
def solution(A):

    A = sorted(A)

    c = 1
    for i in A:
        if i == c:
            c+=1
        else:
            return 0
    return 1

    pass


A = [1,1]
a = solution(A)
print(a)