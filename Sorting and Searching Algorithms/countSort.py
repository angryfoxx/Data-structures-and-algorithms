def countSort(liste):
    dict_ = dict()
    for i in range(len(liste)):
        if liste[i] in dict_:
            dict_[liste[i]] += 1
        else:
            dict_[liste[i]]  = 1
    for i in range(1, 10):
        print(str(i) * dict_[i], end = "")
A = [1, 3, 9, 6, 5, 8, 5, 4, 7, 6, 2, 2, 1]
countSort(A)