def parti(liste, L, H):
    pivot = liste[H]
    j = L - 1
    for i in range(L,H):
        if liste[i] <= pivot:
            j += 1
            liste[i], liste[j] = liste[j], liste[i]
    liste[H], liste[j + 1] = liste[j + 1], liste[H]
    return j + 1

def quickSort(liste, L, H):
    if L < H:
        pi = parti(liste, L, H)
        quickSort(liste, pi + 1, H)
        quickSort(liste, L, pi - 1)
    return liste

A = [6,1,17,22,24,50,41,15,34,28,23,39,40]
print(quickSort(A, 0, len(A) - 1))