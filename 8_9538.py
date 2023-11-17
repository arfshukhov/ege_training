from itertools import *

def c2(c):
    return int(c, 15) % 2 == 0

def c3(c):
    return int(c, 15) % 3 == 0

alpha = "0123456789abcde"

words = ["".join(x) for x in product(alpha, repeat=5)]

cnt = 0

for i in words:
    if i[0] != "0":
        if all((c2(i[0]), c2(i[2]), c2(i[4]))) and all((c3(i[1]), c3(i[3]))):
            cnt += 1
        elif all((c3(i[0]), c3(i[2]), c3(i[4]))) and all((c2(i[1]), c2(i[3]))):
            cnt += 1

print(cnt)