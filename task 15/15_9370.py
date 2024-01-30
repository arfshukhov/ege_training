def f(a, x):
    P = 5 <= x <= 54
    Q = 50 <= x <=93
    return ((not P) and (Q)) <= (x > a)


for a in range(1, 100):
    n = [f(a, x) for x in range(1, 100000)]
    n = list(filter(lambda x: x==0, n))
    if len(n) == 20:
        print(a)
        break