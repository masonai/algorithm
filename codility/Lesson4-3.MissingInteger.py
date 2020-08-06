
def solution(A):
    A = set(A)
    A = sorted(A)

    try:
        a = A.index(1)
        arr = A[a:]
    except:
        return 1

    b = 1
    for i in arr:
        if i == b:
            b += 1
        else:
            return b

    return b

    pass


#A = [1, 3, 6, 4, 1, 2] # return 5
#A = [1, 2, 3] # return 4
#A = [-1, -3, 1, 2, 4] # return 1
A = [-1,-2]
a = solution(A)
print(a)