f = open("/home/user/Загрузки/24_9169.txt").read()

t = []

t_len = []

cnt = 0
for i in range(len(f)-2):
    if f[i]+f[i+1]+f[i+2] in ("BAD", "FAT"):
        t.append(i)


for i in range(2, len(t), 3):
    t_len.append((t[i]+2)-(t[i-2]))


print(min(t_len))