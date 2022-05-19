# insertion sort recursive

def insertionSort(liste,h):
    if len(liste) > 1 and h != len(liste):
        for i in range(h):
            if liste[h] < liste[i]:
                liste[i], liste[h] = liste[h], liste[i]
        return insertionSort(liste, h + 1)
    return liste

A = [6,1,17,22,24,50,41,15,34,28,23,39,40]
B = [6,1,17,22,24,50,41,15,34,28,23,39,45,20,58,6,1,84,3,3,2,5,6874,521,8,3254,31,2]

print(insertionSort(A, 1))
print(insertionSort(B, 1))