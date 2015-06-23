import random
import re

c = 0
def merge(A):
    global c
    q = len(A) / 2
    L = A[:q]
    R = A[q:]

    if len(L) > 1:
        L = merge(L)
    if len(R) > 1:
        R = merge(R)

    i = 0
    j = 0
    res = []

    while len(L) > i and len(R) > j:
        if L[i] <= R[j]:
            res.append(L[i])
            i += 1
        else:
            # print L[i], ">", R[j]
            # print L[i:], '+'
            c += len(L[i:])
            res.append(R[j])
            j += 1

    res += L[i:]
    res += R[j:]
    print c, ' - counter'
    return res


def create_common(a, b):
    lenhgt = len(a)
    fin = [None] * lenhgt
    for elem in a:
        index = a.index(elem)
        index_fin = elem - 1
        fin[index_fin] = b[index]
    return fin


def open_file(num_1, num_2):
    path = "/Users/tarasdmytrus/Documents/Prometeus_algorithms/input_1000_100.txt"
    for line in open(path):
        line = line.split()
        pos = int(line[0])
        numb = (line[1:])
        numb = [int(i) for i in numb]
        if pos == num_1:
            first = numb
        if pos == num_2:
            second = numb
    return first, second

a, b = open_file(951, 178)
# a = [5,4,1,2,3]
# b = [1,3,5,2,4]
# print a   1 5 4 3 2
# print b   5 3 2 1 4
# [5, 4, 1, 2, 3]

comm = create_common(a, b)
# comm = [5, 4, 1, 2, 3]
print a,  ' - first number'
print b,  ' - second number'
print comm , ' - control array' 
merge(comm)




