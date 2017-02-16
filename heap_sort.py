def max_heapify(A, i, heap_size):
    l = 1;
    r = 2;
    if (i != 0):
        l = 2 * i + 1
        r = 2 * i
    largest = i
    if l < heap_size and A[l] > A[largest]:
        largest = l
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)
        
def build_max_heap(A, heap_size):
    for i in range(int(len(A)/2), -1, -1):
        max_heapify(A, i, heap_size)

def heap_sort(A):
    heap_size = len(A)
    build_max_heap(A, heap_size)
    for i in range(len(A) - 1, -1, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, 0, heap_size)

if __name__ == '__main__':
    A = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    print(A)
    heap_sort(A)
    print(A)

# B = [5, 3, 17, 10, 84, 19, 6, 22, 9]
# for i in range(len(B) - 1,  -1, -1):
#     print(i)
# for j in range(0, len(B)):
#     print(j)
# B = [1, 2]
#
# def test(B):
#     B[0], B[1] = B[1], B[0]
#
# test(id(B))
# print(B)
