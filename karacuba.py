counter = 0

def devide(x, y):
    num_1, num_2 = lenght(x, y)
    new_lenght = len(num_1)
    a, b = split_number(num_1)
    c, d = split_number(num_2)
    print a, b, c, d
    return a, b, c, d, new_lenght


def lenght(i, z):
    lenght_1 = len(str(i))
    lenght_2 = len(str(z))

    if lenght_1 - lenght_2 != 0:
        dif = lenght_1 - lenght_2
        if dif < 0:
            i = dif * '0' + str(i)
        else:
            z = dif * '0' + str(z)
        lenght_1 = len(str(i))
        lenght_2 = len(str(z))

    if lenght_1 % 2 != 0:
        new_num_1 = "0" + str(i)
    if lenght_2 % 2 != 0:
        new_num_2 = "0" + str(z)
        return new_num_1, new_num_2
    else:
        return str(i), str(z)


def split_number(num):   # we need to handle 01 - it should be splited to 0 and 1
    num = str(int(num))
    print num, ' --- our num'
    return str(num[:len(num) / 2]), str(num[len(num) / 2:])


def multiply(x, y):
    if int(x) < 10 and int(y) < 10:
        return int(x) * int(y)
    else:
        return karacuba(x, y)


def addition(a, b, c, d, ac, bd):
    print "(", int(a), '+', int(b), ")", "*", '(', int(c), "+", int(d), ")", '-', ac, '-', bd
    return (int(a) + int(b)) * (int(c) + int(d)) - ac - bd


def karacuba(x, y):
    k = 11
    if x < 10 and y < 10:
        return x * y
    else:
        a, b, c, d, t = devide(x, y)
        AC = multiply(a, c)
        BD = multiply(b, d)
        ADBC = addition(a, b, c, d, AC, BD)
        print ADBC, " - ADBC"
        if k == ADBC:
            counter += 1
            print k, '------'

        print 10, '**', t, '*', AC, '+', 10, '**', t, '/', 2, '*', ADBC, '+', BD
        print  (10 ** t) * AC + 10 ** (t / 2) * ADBC + BD
        return (10 ** t) * AC + 10 ** (t / 2) * ADBC + BD

#print karacuba(6421, 98765432,9)
#print karacuba(49823261, 44269423)

print karacuba(1234, 4321)
print counter, ' -number of times was found'







