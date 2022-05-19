def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

A = [6,1,17,22,24,50,41,15,34,28,23,39,40]
B = [6,1,17,22,24,50,41,15,34,28,23,39,45,20,58,6,1,84,3,3,2,5,6874,521,8,3254,31,2]

print(mergeSort(A))
print(mergeSort(B))