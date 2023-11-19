from itertools import *

words = ["".join(x) for x in product("ДЖОБС", repeat=6)]

words = list(filter(lambda x: x.count("Д") == 1 and x.count("О") == 1 and x.count("С") == 1 and x.count("Ж") <= 2, words))

print(len(words))