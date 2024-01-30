f = open("/home/user/Загрузки/24_10105.txt").readline()

idxs = [i for i in range(len(f)) if f[i] == "T"]

mx = 0

for i in range(len(idxs)-101):
    if idxs[i+100] - idxs[i] > mx:
        mx = idxs[i+100] - idxs[i]

print(mx)