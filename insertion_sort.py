A = [5, 2, 4, 6, 1, 3]

for i in range(1, len(A)):
    if A[i - 1] > A[i]:
        key = A[i]
        j = i
        while j > 0 and A[j - 1] > key:
            A[j] = A[j - 1]
            j -= 1
        A[j] = key
    print(i, A)

print(A)


A = (1, 1, 1, 1, 1, 0)

B = (1, 1, 0, 0, 0, 1)

C = [0, 0, 0, 0, 0, 0, 0]

D = (0, 1, 0, 0, 0, 0, 1)

size = len(A)

for i in range(0, size):
    sum = A[i] + B[i] + C[i]
    if sum < 2:
        C[i] = sum
    elif sum == 2:
        C[i] = 0
        C[i + 1] = 1
    else:
        C[i] = 1
        C[i + 1] = 1

print(C)
