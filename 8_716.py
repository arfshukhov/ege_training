from itertools import permutations

alpha = "123456"

words = ["".join(x) for x in permutations(alpha, r=6)]

comb = ["".join(x) for x in permutations("1234", r=4)]

cnt = 0

for i in words:
    for k in comb:
        if k in i:
            cnt += 1
            print(i, k)
            break

print(cnt)