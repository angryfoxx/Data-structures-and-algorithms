"""def shuffle_letters(str1,str2):
    str1_char_dict = dict()
    str2_char_dict = dict()
    for i in str1:

        if i in str1_char_dict:
            str1_char_dict[i] += 1
        else: str1_char_dict[i] = 1

    for j in str2:

         if j in str2_char_dict:
             str2_char_dict[j] += 1
         else: str2_char_dict[j] = 1

    return str1_char_dict == str2_char_dict

print(shuffle_letters("ankara","arxkan"))""" # shuffle letters
"""def shuffle_letters(str1):
    str1_char_dict = dict()
    letter = ""
    for i in str1:
        if i in str1_char_dict:
            str1_char_dict[i] += 1
        else:
            str1_char_dict[i] = 1

    for i,j in zip(str1_char_dict.keys(),str1_char_dict.values()):
        letter += str(j) + j * i
    return letter
print(shuffle_letters("ankara"))""" # letter frequently
"""
def kayipBasamak(str_:str):
    str_splitted = str_.split(" ")
    num_list = []
    forget_data_index = 0
    operator_ = "+"
    if str_splitted[1] == "+": operator_ = "-"
    elif str_splitted[1] == "-": operator_ = "-"
    elif str_splitted[1] == "*":operator_ = "/"
    elif str_splitted[1] == "/":operator_ = "*"

    for i in str_splitted:
        if "x" in i: forget_data_index = str_splitted.index(i)
        try: num_list.append(int(i))
        except: pass

    num_list.sort(reverse=True)
    data = str(int(eval(f"{num_list[0]} {operator_} {num_list[1]}")))

    dicti = dict()
    for i,j in zip(str_splitted[forget_data_index],data):
        if i != j: dicti[i] = j
    return dicti

print(kayipBasamak("20 - 1x = 4"))
print(kayipBasamak("1x0 / 3 = 50"))
print(kayipBasamak("1x * 11 = 121"))
print(kayipBasamak("36 + 1x = 50"))
print(kayipBasamak("36 + 1xyz = 1371"))
""" # kayıp basamak
"""def array_rotation(liste:list):
    string = ""
    for i in (liste[liste[0]:] + liste[:liste[0]]):
        string += str(i)
    return string

print(array_rotation([2,3,4,5]))
print(array_rotation([4,5,6,7,8,9,10,11,12,13]))""" # array rotasyonu
"""def array_pair(liste:list):
    sliced_list = []
    old_value = 0
    for i in range(0,len(liste) + 1,2):
        sliced_list.append(liste[old_value:i])
        old_value = i
    sliced_list.remove([])

    for i in sliced_list:
        if sliced_list.index(i) == sliced_list.index(i[::-1]):
            return i
    return "ok"

print(array_pair([5,6,6,5,3,3]))
print(array_pair([5,6,6,5,8,9,9,8,6,5,5,6]))""" # array pair
"""def wordSplit(liste:list):
    x = list(liste[0])
    for i in range(0,len(x)):
        c = x[::]
        c.insert(i," ")
        if "".join(c).split(" ")[0] in liste[1] and "".join(c).split(" ")[1] in liste[1]:
            return "".join(c).split(" ")

print(wordSplit(["deeplearning", "d,dll,a,deep,dee,base,lear,learning"]))
print(wordSplit(["deeplear2ning", "d,dll,a,deep,dee,base,lear,learning"]))
print(wordSplit(["deeplear2ning", "d,dll,a,deep,dee,base,lear,lear2ning"]))""" # word split
"""def string_tersi_recursion(string:str):
    if len(string) == 1:
        return string
    else:
        return string_tersi_recursion(string[1:]) + string[0]


print(string_tersi_recursion("elma"))
print(string_tersi_recursion("Machine Learning"))
print(string_tersi_recursion("Ömer Faruk Korkmaz"))
print(string_tersi_recursion("lukadruY naaK ahaT"))""" # reverse string with recursion
"""def multiplyRecursive(x, y):
    if y == 1:
        return x
    else:
        return x + multiplyRecursive(x, y - 1)

for i,j in enumerate([5,5,5,5,5,5,5,5,5,5,5]):
    print(multiplyRecursive(i,j))""" # multiply with recursion
"""
def powerRecursive(x,y):
    if y == 1:
        return x
    else:
        return x * powerRecursive(x, y - 1)

for i, j in enumerate(start=1,iterable=list(range(1,10))):
    print(i, j, powerRecursive(i, j))""" # power with recursion
"""def secondGreatLow(arr):
    sorted_list = sorted(set(arr))
    if len(arr) < 2:
        return sorted_list[1],sorted_list[0]
    return sorted_list[1],sorted_list[-2]

print(secondGreatLow([90,4]))
print(secondGreatLow([90,2,1,3,5,5,2,80,60]))""" # second Great Low
"""from itertools import combinations
def threeSum(arr):
    check = 0
    c = 3
    for i in combinations(arr[1:],c):
        if sum(i) == arr[0]:
            check += 1
    if check >= c:
        return True
    return False

A = [10, 2, 3, 1, 5, 3, 1, 4, -4, -3, -2]
print(threeSum(A))

B = [12, 3, 1, -5, -4, 7]
print(threeSum(B))""" # three sum
"""def vertexCovering(liste:list):
    failed = []
    vertices = liste[-1][1:-1].split(",")
    graph = liste[1][1:-1].split(",")
    if len(vertices[0]) == 0:
        return liste[1]
    for i in graph:
        flag = True
        for j in vertices:
            if j in i:
                flag = False

        if flag:
            failed.append(i)

    if len(failed) == 0:
        return "yes"
    return failed

print(vertexCovering(["(A,B,C,D)","(A-B,A-D,B-D,A-C)","(A,B)"]))
print(vertexCovering(["(A,B,C,D)","(A-B,A-D,B-D,A-C)","(C)"]))
print(vertexCovering(["(A,B,C,D)","(A-B,A-D,B-D,A-C)","(C,B)"]))
""" # vertex covering
"""
def catalanNumbers(n):
    if n <= 1:
        return 1

    toplam = 0
    for i in range(n):
        toplam += catalanNumbers(i) * catalanNumbers(n - i - 1)

    return toplam


for i in range(10):
    print(catalanNumbers(i))
""" # catalan numbers
"""def dynamicFibo(n):
    fiboList, i = [0, 1], 2

    while len(fiboList) < n:
        fiboList.append(fiboList[i - 2] + fiboList[i - 1])
        i +=1

    return fiboList

print(dynamicFibo(10))""" # fibonacci with dynamic