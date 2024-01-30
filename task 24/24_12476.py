import re

f = open("/home/user/Загрузки/24_12476.txt").readline()

f = f.replace("ORO", "2").replace("ROR", "2").replace("RO", "1")

f1 = f.split("2")

f1.sort(key=lambda x: x.count("1"))

f2 = set()

list(f2).sort(key=lambda x: len(x))

print(f2)