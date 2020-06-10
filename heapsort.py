def heapsort(arr):
    """Perform heap sort on given array. Is modify order of elements in array.
    """

    def shift_down(i, n):
        while True:
            j = i
            if 2*j <= n and arr[2*j-1] > arr[i-1]:
                i = 2*j
            if 2*j+1 <= n and arr[2*j] > arr[i-1]:
                i = 2*j+1
            if j == i:
                break
            arr[j-1], arr[i-1] = arr[i-1], arr[j-1]

    n = len(arr)
    for i in range(n//2, 0, -1):
        shift_down(i, n)

    for i in range(n, 0, -1):
        arr[0], arr[i-1] = arr[i-1], arr[0]
        shift_down(1, i-1)
