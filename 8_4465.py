from itertools import *

alpha = "ДЕЙНПТЬЯ"

words = ["".join(x) for x in product(alpha, repeat=4)]


print(words.index("ЬТПН"))