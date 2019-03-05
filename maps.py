def mapi(f, l):
    z = []
    for i in l:
        z.append(f(i))
    return z


def fun(i):
    return i+1


print(mapi(fun(0), [1, 3, 4]))
