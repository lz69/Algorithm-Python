def counting_sort(A, B, k):
    C = list()
    for i in range(0, k):
        C.append(0)
    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1

if __name__ == '__main__':
    A = [2, 5, 3, 0, 2, 3, 0, 3]
    k = 6
    B = [0, 0, 0, 0, 0, 0, 0, 0]
    print(A)
    counting_sort(A, B, 6)
    print(B)
