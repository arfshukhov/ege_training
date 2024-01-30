def f(a, x, y):
     return (x<a)or(y<a)or(x+2*y>50)


for a in range(1, 1000):
    if all([f(a, x, y) for x in range(1, 1000) for y in range(1, 1000)]):
        print(a)
        break