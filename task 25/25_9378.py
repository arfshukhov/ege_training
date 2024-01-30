from fnmatch import *


for i in range(0, 10**12+1, 4013):
    if fnmatch(str(i), "123?4*5679"):
        print(i, i//4013)

