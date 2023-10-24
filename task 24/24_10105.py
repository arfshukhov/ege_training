from string import ascii_uppercase
import re

file = open("/home/user/Загрузки/24_10105.txt", "r").read()

delim = "|".join([ "U", "V", "W", "X", "Y",  "Z"])

tokens = re.split(delim, file)

tokens = list(filter(lambda x: len(x) >= 100, tokens))
tokens.sort(key=lambda x: len(x))
print(len(tokens[-1]))