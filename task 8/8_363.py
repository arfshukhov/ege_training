from itertools import *


words = ["".join(x) for x in product("АКЛОШ", repeat=5)]

words = list(filter(lambda x: x.count("О") > 0 or x.count("А") > 0, words))

print(len(words))