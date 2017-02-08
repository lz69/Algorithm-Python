A = [2, 4, 5, 7, 1, 2, 3, 6]

for i in range(0, len(A) - 1 - 1):
    for j in range(len(A) - 1, i, -1):
        if A[j] < A[j - 1]:
            temp = A[j]
            A[j] = A[j-1]
            A[j-1] = temp
    print(A)
