# bubble sort recursive

def bubbleSort(arr, H):
    if H > 0:
        check = 0
        for i in range(H):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                check = i
        if check:
            return bubbleSort(arr, H - 1)
    return arr


A = [6, 1, 17, 22, 24, 50, 41, 15, 34, 28, 23, 39]
B = [6, 1, 17, 22, 24, 50, 41, 15, 34, 28, 23, 39, 45, 20, 58, 6, 1, 84, 3, 3, 2, 5, 6874, 521, 8, 3254, 31, 2]

print(bubbleSort(A, len(A) - 1))
print(bubbleSort(B, len(B) - 1))