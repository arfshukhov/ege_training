def d(n, m):
    return n % m == 0

def f(a, x):
    B = 120 <= x <= 130
    return (B <= (not d(x, 7))) or (a > 2*x)


for a in range(1, 1000):
    if all([f(a, x) for x in range(1000)]):
        print(a)
        break