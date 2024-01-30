def f(n):
    return g(n-1)

def g(n):
    if n < 10:
        return n
    else:
        return g(n-2)+1


quads = [x**2 for x in range(1,101)]

c = 0
for i in range(101):
    if g(i) in quads:
        c += 1

print(c)