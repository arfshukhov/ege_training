from itertools import *

alpha = "01234"

A = ["".join(x) for x in product(alpha, repeat=5)]

B = ["".join(x) for x in product(alpha, repeat=5)]

res = set()

for a in A:
    for b in B:
        if int(a,5) > int(b, 5) and a[0] != "0" and b[0] != "0":
            res.add(int(a, 5) - int(b, 5))

print(len(res))