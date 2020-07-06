# #####################################################################################################################
# Question 2
# Sequence Arithmetic

"""Takes in two lists. Loops through the values in both using one index and adds them together. Then we append that
value to the empty list z and return """


def seqaddi(x, y):
    z = []
    for i in range(mylength(x)):
        z += [(x[i]) + (y[i])]
    return z


"""Takes in two lists. Loops through the values using one index and multiply at every element in each list. We then 
append to z and return z """


def seqMulti(x, y):
    z = []
    for xIndex in range(mylength(x)):
        z = z + [(x[xIndex]) * (y[xIndex])]
    return z


"""My implementation of len which will loop through the list x and adds 1 to a counter everytime it loops"""


def mylength(x):
    n = 0
    for i in x:
        n += 1
    return n


"""Takes in two lists. Finds out if one list has no items return the other list. Otherwise we return first index 
added to the other lists first index and call the function on the next list index """


def seqaddr(x, y):
    if not x:
        return y
    elif not y:
        return x
    else:
        return [x[0] + y[0]] + seqaddr(x[1:], y[1:])


"""Takes in two lists. Finds out if one list has no items return the other list. Otherwise we return first index 
multiplied to the other lists first index and call the function on the next list index """


def seqmultr(x, y):
    if not x:
        return y
    elif not y:
        return x
    else:
        return [x[0] * y[0]] + seqmultr(x[1:], y[1:])


"""Take in two lists, return the list of the list item added to the respecting item in the other list whilst looping 
through the list """


def seqaddc(x, y):
    return [x[i] + y[i] for i in range(mylength(x))]


"""Take in two lists, return the list of the list item Multiplied to the respecting item in the other list whilst looping 
through the list """


def seqmultc(x, y):
    return [x[i] * y[i] for i in range(mylength(x))]


print("SEQUENCE ARITHMETIC TESTS")
print("Expected [2,1,4]")
print(seqaddi([3, 2, 2], [-1, -1, 2]))
print("Expected [-1,4,6]")
print(seqMulti([1, 2, 3], [-1, 2, 2]))
print("Expected [2,4,6]")
print(seqaddr([3, 2, 3], [-1, 2, 3]))
print("Expected [3,4,3]")
print(seqmultr([1, 2, 3], [3, 2, 1]))
print("Expected [4,1,4]")
print(seqaddc([5, -2, 3], [-1, 3, 1]))
print("Expected [-5,-6,3]")
print(seqmultc([5, -2, 3], [-1, 3, 1]))
print("Expected [error] for all test with lists of different lengths")
print(seqaddi([3, 2, 2], [-1, -1]))




