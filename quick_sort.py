import random


global compare
compare = 0


def partition(lst, p, r):
    global compare

    pivot = lst[r]
    i = p - 1
    for j in lst[p:r]:
        compare += 1
        if j <= pivot:
            i += 1
            ind = lst.index(j)
            lst[i], lst[ind] = lst[ind], lst[i]

    lst[r], lst[i + 1] = lst[i + 1], lst[r]
    return i + 1, lst


def quick(lst, p, r):
    if p < r:
        # lst = swap(lst, p, r)
        lst = mediana(lst, p, r)
        q, lst = partition(lst, p, r)
        lst = quick(lst, p, q - 1)
        lst = quick(lst, q + 1, r)
        return lst
    else:
        return lst


def swap(lst, p, r):
    last = lst[r]
    first = lst[p]
    lst[p] = last
    lst[r] = first
    return lst


def mediana(lst, p, r):
    med = (r + p) / 2
    if len(lst) == 2:
        med = lst[0]

    lst_med = [lst[p], lst[med], lst[r]]
    lst_med.sort()
    med = lst.index(lst_med[1])
    lst = swap(lst, med, r)
    return lst


def read_file():
    a = []
    with open('./data_examples_03/sharp_numb.txt') as l:
        for line in l:
            a.append(int(line.rstrip()))
    return a


def randomise():
    a = range(10)
    random.shuffle(a)
    print a, ' ++++'

a = read_file()

quick(a, 0, (len(a) - 1))
print compare, " amounth of comparisons"











