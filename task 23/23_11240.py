def f(cur, end, last):
    if cur == end:
        return 1
    if cur > end:
        return 0
    if cur < end:
        if last == "B":
            return f(cur+2, end, "A")+f(cur*3, end, "C")
        else:
            return f(cur+2, end, "A")+f(cur**2, end, "B")+f(cur*3, end, "C")


print(f(2, 64, ""))

