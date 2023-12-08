def f(h, t):
    if h >= 111:
        return t%2==0
    if t == 0:
        return 0
    m = [f(h+1, t-1), f(h+3, t-1), f(h*4, t-1)]
    return any(m) if t%2 != 0 else all(m)


for i in range(1, 111):
    if not f(i, 1) and f(i, 2):
        print(i)
        break

print([x for x in range(1, 111) if not f(x, 1) and f(x, 3)][:2])


print([x for x in range(1, 111) if f(x, 4)][0])