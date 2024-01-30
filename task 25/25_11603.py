from fnmatch import *
f = list()
for i in range(0, 10**12+1, 596):
    if fnmatch(str(i), "1*28?64"):
        f.append(i)

print(len(f), sum(f)//len(f))

