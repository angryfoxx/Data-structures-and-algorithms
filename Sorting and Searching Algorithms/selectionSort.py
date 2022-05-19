def selectionSort(liste):
    for j in range(len(liste)):
        #lowest_number = liste[j]
        lowest_number = j
        for i in range(j, len(liste)):
            if liste[i] < liste[lowest_number]:
                 lowest_number = i
            #if liste[i] < lowest_number:
                #lowest_number = liste[i]
        #il = liste[j::].index(lowest_number) + j
        #liste[j], liste[il] = liste[il], liste[j]
        liste[j], liste[lowest_number] = liste[lowest_number], liste[j]
    return liste

A = [6,1,17,22,24,50,41,15,34,28,23,39,40]
B = [6,1,17,22,24,50,41,15,34,28,23,39,45,20,58,6,1,84,3,3,2,5,6874,521,8,3254,31,2]

print(selectionSort(A))
print(selectionSort(B))