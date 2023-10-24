from string import ascii_uppercase
import re
delim = "|".join(list(ascii_uppercase[6:]))
print(delim)


file = open("/home/user/Загрузки/24_10724.txt" , "r").read()
tokens = re.split(delim, file)

tokens = list(filter(lambda x: len(x) != 0, tokens))
tokens = list(map(lambda x: str(x).lstrip("0"), tokens))
tokens.sort(key=lambda x: len(x))

print(len(tokens[-1]))
