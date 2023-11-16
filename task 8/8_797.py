from itertools import *

alpha = "ЧИСТЫЙРАЗУМ"

words = ["".join(x) for x in product(alpha, repeat=5)]

words = list(filter(lambda x: x.count("Й") <= 1, words))

print(len(words))