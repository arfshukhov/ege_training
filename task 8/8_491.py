from itertools import *

words = ["".join(x) for x in product("АВДПР", repeat=4)]

print(words.index("ВДПР")+1)