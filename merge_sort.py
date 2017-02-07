import sys

sys.setrecursionlimit(1500)

def merge(A, p, q, r):
    L = []
    R = []
    for i in range(p, q):
        L.append(A[i])
    L.append(sys.maxsize)
    for i in range(q, r):
        R.append(A[i])
    R.append(sys.maxsize)
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p, r):
    if p < r:
        q = int((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

if __name__ == '__main__':
    A = [2, 4, 5, 7, 1, 2, 3, 6]
    merge_sort(A, 0, len(A) - 1)
    print(A)
