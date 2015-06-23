import string
import pdb

global alphabet

def reader():
    input_list = []
    with open('./radix_input.py') as f:
        for line in f:
            input_list.append(line.rstrip())
    return input_list


def char_gen():
    alphabet = []
    for char in string.ascii_lowercase:
        alphabet.append(char)
    return alphabet


def convert(char):
    global alphabet
    if type(char) == int:
        return alphabet[int]
    else:
        return alphabet.index(char)


def radix(input_list, radix, maxValue):
    global alphabet

    array = input_list
    for rad in range(radix - 1, -1, -1):
        array = linear_sort(array, rad, maxValue)
    return array


def linear_sort(arr, rad, maxValue):
    global alphabet
    fin = [0] * len(arr)
    c = [0] * maxValue                            # initialising empty temporary list
    for i in range(len(arr)):               # count appearings of each possible
        c[convert(arr[i][rad])] += 1         # number

    for i in range(1, maxValue):                   # counting all presiding amounth of items
        c[i] = c[i] + c[i - 1]

    for j in range(len(arr) - 1, -1, -1):
        fin[c[convert(arr[j][rad])] - 1] = arr[j]
        c[convert(arr[j][rad])] = c[convert(arr[j][rad])] - 1
    return fin

a = ["hzt", "sng", "ena", "sdt", "qds", "yif",
     "slt", "lpz", "cqc", "hpo"]
alphabet = char_gen()
rang = len(alphabet)   # maximum list length - one letter one element

print radix(a, 3, rang)
