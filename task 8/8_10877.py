from itertools import *;print(len(list(filter(lambda x: x.count("З")==1, ["".join(x) for x in product("ПРИКАЗ", repeat=4)]))))