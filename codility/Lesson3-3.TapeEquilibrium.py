
def solution(A):
    if len(A) == 1:
        return A[0]

    total_sum = sum(A)

    left_sum = 0
    diff_list = []
    for i in range(len(A)-1):
        left_sum += A[i]
        right_sum = total_sum - left_sum

        diff = abs(left_sum - right_sum)
        diff_list.append(diff)

    return min(diff_list)

    pass


A = [3,1,2,4,3]
a = solution(A)


