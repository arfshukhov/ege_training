from itertools import *

aplha = "0123456789abcdef"

words = ["".join(x) for x in product(aplha, repeat=5)]

cnt = 0
for i in words:
    if i.count("6") == 2 and i[0] != "0":
        for x in "0248ace":
            i = i.replace(x, "n")
        if "n6" not in i and "6n" not in i and "66" not in i: cnt +=1

print(cnt)
