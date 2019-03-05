# ######################################################################################################################
# Question 8
# Datums


def mylength(x):
    n = 0
    for i in x:
        n += 1
    return n


def gendat(x):
    z = []
    if not x:
        return []
    elif type(x) != type([x]):
        z += [x]
        return z
    else:
        for maini in range(mylength(z)):
            if isinstance(x[maini], []):
                return


print(gendat([5, [5, []], [], [5]]))
print(gendat([]))
print(gendat(5))
