import random


def sgreg(A):
    if 100 <= A <= 999:

        al = 'QWERTYUIOPASDFGHJKLZXCVBNM0123456789'
        a = ''
        a += al[random.randint(0, 35)]
        a += al[random.randint(0, 35)]
        a += al[random.randint(0, 35)]
        a += al[random.randint(0, 35)]
        a += al[random.randint(0, 35)]
        # print(a)

        d = a[3:]
        b = a[1:] + '-'
        a += '-'
        c = b[1:]
        return (a + b + c + d)
    else:
        return 'Wrong! Please enter a three-digit number.'
