def f(cur, end):
    if cur == end:
        return 1
    if cur > end or cur == 16:
        return 0
    if cur < end:
        return f(cur+2, end)+f(cur*3, end)+f(cur*2, end)


print(f(13,45))