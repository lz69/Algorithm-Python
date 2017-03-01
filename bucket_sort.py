def bucket_sort(A):
    n = len(A)
    B = list()
    C = list()
    for i in range(n):
        B.append(list())
    for i in range(n):
        j = int(A[i] / 10)
        B[j].append(A[i])
        B[j].sort()
    for i in range(len(B)):
        for j in range(len(B[i])):
            C.append(B[i][j])
    print(C)

if __name__ == '__main__':
    A = [78, 17, 39, 26, 72, 94, 21, 12, 23, 68]
    bucket_sort(A)
