from itertools import *

aplha = "0123456789abc"

words = ["".join(x) for x in product(aplha, repeat=6)]

cnt = 0
for i in words:
    if i.count("5") <= 1 and i[0] != "0":
        for x in "13579b":
            i = i.replace(x, "n")
        if "nn" not in i: cnt +=1

print(cnt)
