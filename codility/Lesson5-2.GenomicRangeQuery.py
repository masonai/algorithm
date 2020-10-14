

def solution(S, P, Q):
    M = len(P)
    result = []

    for i in range(M):
        begin = P[i]
        end = Q[i] + 1
        new_arr = S[begin:end]

        if new_arr.find("A") != -1:
            result.append(1)
        elif new_arr.find("C") != -1:
            result.append(2)
        elif new_arr.find("G") != -1:
            result.append(3)
        elif new_arr.find("T") != -1:
            result.append(4)
        else:
            pass

    return result


# ACGT = 1234
S = 'CAGCCTA'
#S = 'GGGGGGGGG'
P = [2, 5, 0]
Q = [4, 5, 6]


a = solution(S, P, Q)
print(a)