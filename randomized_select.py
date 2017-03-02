import quick_sort as qs

def randomized_select(A, p, r, i):
    if p == r:
        return A[p]
    q = qs.random_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q-1, i)
    else:
        return randomized_select(A, q+1, r, i-k)


if __name__ == '__main__':
    A = [2, 8, 7, 1, 3, 5, 6, 4]
    print(randomized_select(A, 0, len(A) - 1, 1))
