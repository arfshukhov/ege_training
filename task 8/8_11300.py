from itertools import product

alpha = "БГДНОУШ"

words = ["".join(x) for x in product(alpha, repeat=6)]

idxs = [i for i, k in enumerate(words) if k[0] != "Б" and k.count("Н") >= 2 and "У" not in k]

print(max(idxs)+1)
