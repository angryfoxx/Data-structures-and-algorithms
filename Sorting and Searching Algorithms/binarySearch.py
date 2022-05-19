# binary search recursive

def binarySearch(liste, L, H, number):
    M = (H - L) // 2 + L
    if H >= L:
        if liste[M] != number:
            if liste[M] < number:
                return binarySearch(liste, M + 1, H, number)
            else:
                return binarySearch(liste, L, M - 1, number)
        return f"Listenin {M}. indexi: {liste[M]}"
    else: return -1

liste = [2,3,4,5,6,7,8,9,10,11,12,13,15,16,18,19,20]

print(binarySearch(liste, 0, len(liste) - 1, 7))
print(binarySearch(liste, 0, len(liste) - 1, 13))
print(binarySearch(liste, 0, len(liste) - 1, 22))