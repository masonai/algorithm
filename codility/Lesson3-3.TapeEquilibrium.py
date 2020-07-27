
def solution(A):
    if len(A) == 1:
        return A[0]

    diff = []
    for i in range(len(A)-1):
        s = i+1

        t1 = A[:s]
        t2 = A[s:]
        s1 = sum(t1)
        s2 = sum(t2)

        if abs(s1-s2) == 0:
            return 0
        '''
        s1, s2 = 0, 0
        for t in t1:
            s1 += t
        for t in t2:
            s2 +=t
        '''
        diff.append(abs(s1-s2))

    return min(diff)

    pass


A = [1,1,1]
r = solution(A)
print(r)