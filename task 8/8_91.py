from itertools import *

words = list(filter(lambda x: "КОТ" in x, ["".join(x) for x in product("ЕИЙКНОТ", repeat=7)]))

print(len(words))

