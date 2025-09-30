def ChoosePivot(A, low, high):
    midt= (low + high)//2

    a = A[low]
    b = A[midt]
    c = A[high]

    if (a<= b <=c ) or (c<= b <= a):
        return midt
    elif (b<= a<= c) or (c<= a <= b):
        return low
    else:
        return high


def Partition(A, low, high):
    p = ChoosePivot(A, low, high)
    A[p], A[high] = A[high], A[p]

    pivot = A[high]
    left = low
    right = high - 1

    while left <= right:
        while left <= right and A[left] <= pivot:
            left = left +1
        while right >= left and A[right] >= pivot:
            right = right-1
        if left < right:
            A[left], A[right] = A[right], A[left]
            left+=1
            right-=1
    A[left], A[high] = A[high], A[left]

    return left

def Quicksort(A, low, high):
    if low >= high:
        return A
    
    p = Partition(A, low, high)
    Quicksort(A, low, p-1)
    Quicksort(A, p+1, high)
    return A
