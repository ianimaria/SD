import random
import math
import time


def BubbleSort(v):
    start = time.time()
    for i in range(len(v)):
        for j in range(0, len(v) - i - 1):
            if v[j] > v[j + 1]:
                aux = v[j]
                v[j] = v[j + 1]
                v[j + 1] = aux
            now = time.time()
            if now - start > 20:
                return 0
    return v


def CountSort(v):
    frecv = [0 for i in range(max(v) + 1)]
    sort = []
    for i in range(len(v)):
        frecv[v[i]] = frecv[v[i]] + 1
    for i in range(len(frecv)):
        for j in range(frecv[i]):
            sort.append(i)
    return sort


def CountSortDigit(v, cif, radix=10):
    sort = [0] * len(v)
    count = [0] * radix
    for i in range(len(v)):
        cifra = (v[i] // radix ** cif) % radix
        count[cifra % radix] = count[cifra % radix] + 1
    for i in range(1, radix):
        count[i] += count[i - 1]

    for i in range(len(v) - 1, -1, -1):
        cifra = (v[i] // radix ** cif) % radix
        count[cifra] = count[cifra] - 1
        sort[count[cifra]] = v[i]
    return sort


def RadixSort(v):
    m = max(v)
    sort = v.copy()
    digits = int(math.floor(math.log(m, 10) + 1))
    for i in range(digits):
        sort = CountSortDigit(sort, i)
    return sort


def Interclasare(lst, ldr):
    i = j = 0
    rez = []
    while i < len(lst) and j < len(ldr):
        if lst[i] <= ldr[j]:
            rez.append(lst[i])
            i = i + 1
        else:
            rez.append(ldr[j])
            j = j + 1
    rez.extend(lst[i:])
    rez.extend(ldr[j:])
    return rez


def MergeSort(v):
    if len(v) <= 1:
        return v
    else:
        mij = len(v) // 2
        lst = MergeSort(v[:mij])
        ldr = MergeSort(v[mij:])
        return Interclasare(lst, ldr)


def pivot_mediana(v):
    if len(v) <= 5:
        return sorted(v)[len(v) // 2]
    subliste = [sorted(v[i:i + 5]) for i in range(0, len(v), 5)]
    mediane = [sl[len(sl) // 2] for sl in subliste]
    return pivot_mediana(mediane)


def QuickSort(v):
    if len(v) == 0:
        return []
    if len(v) == 1:
        return v
    pivot = pivot_mediana(v)
    L = [x for x in v if x < pivot]
    E = [x for x in v if x == pivot]
    G = [x for x in v if x > pivot]

    L = QuickSort(L)
    G = QuickSort(G)
    L.extend(E)
    L.extend(G)

    return L


def TestSort(v):
    global l
    c = l.copy()
    c.sort()
    if v == c:
        return "Sortarea este corecta"
    else:
        return "Sortarea nu este corecta"


currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name

f = open("input.txt", 'r')
t = int(f.readline())
sorts = [sorted, BubbleSort, CountSort, RadixSort, MergeSort, QuickSort]

for i in range(t):

    nr, M = f.readline().split()
    nr, M = int(nr), int(M)
    print()
    print("Test", i + 1, "(S-au testat %s numere cu valori pana la %s)" % (nr, M))
    print()
    v = [0] * nr
    if nr == 0:
        print("Vectorul nu are elemente")
    elif nr != 0 and M != 0:
        for j in range(nr):
            x = random.choice(range(M))
            v[j] = x
        l = v.copy()

        for sort in sorts:
            v = l.copy()
            start = time.time()
            s = sort(v)
            end = time.time()
            if end - start >= 20:
                print(sort.__name__, ":", "Sortarea dureaza mai mult de 20 de secunde")
            else:
                print(sort.__name__, ":", round(end - start, 3), TestSort(s))
    else:
        print("Vectorul are toate elementele 0")