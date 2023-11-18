from itertools import product

words = ["".join(x) for x in product("ГЕКЭ023", repeat=4)]

for i, k in enumerate(words):
    if k[0] == "0" and "ГГ" not in k and "ЕЕ" not in k and "КК" not in k and "ЭЭ" not in k and "00" not in k\
            and "22" not in k and "33" not in k:
        print(i+1)
        break
