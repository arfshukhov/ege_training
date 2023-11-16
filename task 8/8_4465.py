from itertools import *

alpha = "ДЕЙНПТЬЯ"

words = ["".join(x) for x in product(alpha, repeat=4)]

cnt = 0

for k, i in enumerate(words):
    if "Я" not in i and "Е" not in i and "".join(list(i)) == "".join(set(i)):
        cnt = k+1

print(cnt)