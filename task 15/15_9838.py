def f(a, x, y):
    return (x + 2 * y > a) or (y < x) or (x < 30)

for a in range(1000, 0, -1):
    if all([f(a, x, y) for x in range(100) for y in range(100)]):
        print(a)
        break