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
