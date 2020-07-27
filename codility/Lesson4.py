def solution(X, Y, D):
    a = (Y - X) / D

    if a % 1 == 0:
        return int(a)
    else:
        return int(a) + 1

    pass


X = 10
Y = 85
D = 30
a = solution(X, Y, D)
print(a)
