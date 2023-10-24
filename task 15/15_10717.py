def tr(m, n, k):
    return (m < (n + k)) and (n < (m+k)) and (k < (m + n))


def m(a, b):
    if a > b:
        return a
    else:
        return b


def f(a, x):
    return not ((tr(x, 11, 18) == (not (m(x, 5) > 68))) and (tr(x, a, 5)))


for a in range(100, 0, -1):
    if all(f(a, x) for x in range(100)):
        print(a)