from itertools import *

words = ["".join(x) for x in product("ВАСЯ", repeat=5)]

words = list(filter(lambda x: x.count("А") >= 1, words))

print(len(words))