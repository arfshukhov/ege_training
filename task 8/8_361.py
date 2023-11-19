from itertools import *

words = list(filter(lambda x: x.count("А") <= 1, ["".join(x) for x in product("СЧИТАЙ", repeat=4)]))

print(len(words))
