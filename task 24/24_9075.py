file = open("/home/user/Загрузки/24_9075.txt").read()

t = []

t_len = []

for i in range(10):
    if i % 2 == 0:
        file = file.replace(str(i), "Ч")
    else:
        file = file.replace(str(i), "Н")


for i in range(len(file)-1):
    if file[i]+file[i+1] in ("ЧН", "НЧ"):
        t.append(i)

for i in range(1, len(t), 2):
    t_len.append((t[i]+1)-(t[i-1]))


print(max(t_len)-1)