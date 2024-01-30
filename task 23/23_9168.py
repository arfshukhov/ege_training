res = set()


def f(cur, c):
    if c == 4:
        res.add(cur)
        return 0
    if c < 4:
        f(cur+2, c+1)
        f(cur*3, c+1)


f(1, 0)
print(len(res))