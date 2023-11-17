from itertools import permutations

words = ["".join(x) for x in permutations("ВЕБИНАР", r=7)]

cnt = 0

for i in words:
    for a in "ВБНР":
        i = i.replace(a, "S")
    for b in "ЕИА":
        i = i.replace(b, "G")
    if "SS" not in i and "GG" not in i:
        cnt += 1

print(cnt)