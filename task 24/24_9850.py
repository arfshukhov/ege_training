import re

file = open("/home/user/Загрузки/24_9850.txt", "r").read()

delim = "|".join(["L", "I", "S", "E", "N", "O", "K"])

tokens = list(filter(lambda s: len(s) > 0, re.split(delim, file)))
tokens.sort(key=lambda x: len(x), reverse=True)

print(len(tokens[0]))




