def solution(A):
    check = {}
    for i in A:
        try:
            check[i] += 1
        except:
            check[i] = 1

    for i in check:
        if check[i] % 2 == 1:
            return i

    pass


A = [9, 3, 9, 3, 9, 7, 9]

r = solution(A)
print(r)
