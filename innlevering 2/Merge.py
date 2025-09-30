def MergeSort(A):
    n = len(A)
    if n <= 1:
        return A
    i = (n//2)
    Array1 = MergeSort(A[:i])
    Array2 = MergeSort(A[i:])
    return Merge(Array1, Array2, A)


def Merge(Array1, Array2, A):
    i = 0
    j = 0
    while i < len(Array1) and j < len(Array2):
        if Array1[i] <= Array2[j]:
            A[i+j] = Array1[i]
            i = i + 1
        else:
            A[i+j] = Array2[j]
            j = j + 1
    while i < len(Array1):
        A[i + j] = Array1[i]
        i = i + 1
    while j < len(Array2):
        A[i + j] = Array2[j]
        j = j + 1
    return A
