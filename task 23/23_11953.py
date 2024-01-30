from numba import njit

@njit(None)
def f(cur, end):
    if cur > end or cur == 100:
        return 0
    if cur == end:
        return 1
    if cur < end:
        if cur%10==0:
            return f(cur+cur%68, end)+f(cur**2, end)
        elif cur%68 == 0:
            return f(cur+cur%10, end)+f(cur**2, end)
        else:
            return f(cur+cur%10, end)+f(cur+cur%68, end)+f(cur**2, end)


print(f(2, 68)*f(68,680))