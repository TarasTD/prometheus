import pdb


def reader():
    input_list = []
    with open('./radix_input.py') as f:
        for line in f:
            input_list.append(line.rstrip())
    return input_list


def radix(input_list, radix, maxNumber):
    array = input_list
    for rad in range(radix - 1, -1, -1):
        array = linear_sort(array, rad, maxNumber)
        print array
    return array


def linear_sort(arr, rad, maxNumber):
    fin = [0] * len(arr)
    c = [0] * maxNumber               # initialising empty temporary list
    for i in range(len(arr)):  # counting appearings of each possible
        c[int(arr[i][rad])] += 1         # number

    for i in range(1, maxNumber):      # counting all presiding amounth of items
        c[i] = c[i] + c[i - 1]

    for j in range(len(arr) - 1, -1, -1):
        pdb.set_trace()
        fin[c[int(arr[j][rad])] - 1] = arr[j]
        c[int(arr[j][rad])] = c[int(arr[j][rad])] - 1
    return fin

a = ['345', '241', '121', '614', '115', '162', '218', '495', '101']
rang = 10

print radix(a, 3, rang)
