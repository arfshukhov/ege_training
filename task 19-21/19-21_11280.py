def f(h, m):
    if h >= 199:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(h+1, m-1), f(h+5, m-1), f(h*3, m-1)]
    return any(h) if m%2!=0 else any(h)


print("19: ", min([x for x in range(1,199) if f(x, 2)]))


def f(h, m):
    if h >= 199:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(h+1, m-1), f(h+5, m-1), f(h*3, m-1)]
    return any(h) if m%2!=0 else all(h)


print("20: ", *[x for x in range(1,199) if not f(x, 1) and f(x, 3)][:2])

print("21: ", min([x for x in range(1, 199) if not f(x, 2) and f(x, 4)]))