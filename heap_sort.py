def max_heapify(A, i):
    l = 1;
    r = 2;
    if (i != 0):
        l = 2 * i + 1
        r = 2 * i
    largest = i
    if l < len(A) and A[l] > A[largest]:
        largest = l
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)
    print(A)

if __name__ == '__main__':
    A = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    print(A)
    max_heapify(A, 0)
    print(A)

# B = [1, 2]
#
# def test(B):
#     B[0], B[1] = B[1], B[0]
#
# test(id(B))
# print(B)
