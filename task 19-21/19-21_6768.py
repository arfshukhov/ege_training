def f(h, t):
    if h >= 59:
        return t%2==0
    if t == 0:
        return 0
    m = [f(h+1, t-1), f(h+4, t-1), f(h*3, t-1)]
    return any(m) if t%2!=0 else all(m)
print([x for x in range(1, 59) if not f(x, 1) and
print([x for x in range(1, 59) if not f(x, 1) and
print([x for x in range(1, 59) if f(x, 4)][0])
