from itertools import product

alpha = "БМНРЮ"

words = ["".join(x) for x in product(alpha, repeat=6)]

idxs = [i+1 for i, k in enumerate(words) if k[0] != "М" and k.count("Р") >= 2 and "Ю" not in k]

print(max(idxs))
