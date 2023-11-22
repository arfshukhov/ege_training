import string
import re

file = open("/home/user/Загрузки/24_9552.txt").read()

delim = "|".join(list(string.ascii_uppercase))

file = file.replace("PC", "2")
file = file.replace("CSGO", "4")

file = re.split(delim, file)
f1 = list()

for i in file:
    f1.append(sum(list(map(int, list(i)))))

print(max(f1))
