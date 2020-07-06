# ######################################################################################################################
# # Question 3
# # Matrices



def mylength(x):
    n = 0
    for i in x:
        n += 1
    return n


"""MY implementation of all. Takes in a list or matrix and returns true if there if another element in the list 
otherwise false """


def myAll(lstX):
    for element in lstX:
        if not element:
            return False
    return True


# QUESTION 3a


"""Takes in a matrix. Sets the first list in the matrix to l1. We loop through the matrix and see if the length of 
each list is equal to l1. We use myAll to find out when to stop looping. If they are all equal the return true 
otherwise false """


def isMatrix(x):
    l1 = mylength(x[0])
    if myAll(mylength(i) == l1 for i in x[1:]):
        return True
    else:
        return False


"""We take in the matrix. Check if it is a matrix, if it is then loop through the matrix to find the rows, 
then loop through list 0 to find the columns as we know all the columns will be the same as wwe have confirmed that 
it is a matrix """


# QUESTION 3b


def matrixShape(x):
    rows = 0
    cols = 0
    if isMatrix(x):
        for i in x:
            rows += 1
        for j in x[0]:
            cols += 1
        return rows, cols
    return "This ain't a matrix mate"


def seqaddr(x, y):
    if not x:
        return y
    else:
        return [x[0] + y[0]] + seqaddr(x[1:], y[1:])


def seqmultr(x, y):
    if not x:
        return y
    elif not y:
        return x
    else:
        return [x[0] * y[0]] + seqmultr(x[1:], y[1:])


# QUESTION 3c


"""Take in the two matrices, check if they are both matrices then loop through x and use seqaddr from Q2b to add each 
of the lists in each in matrix. Then we append the values to list z. If we find they are not matrices then return 
This ain't a matrix mate """


def addMatrix(x, y):
    if isMatrix(x):
        if isMatrix(y):
            if matrixShape(x) == matrixShape(y):
                z = []
                for i in range(mylength(x)):
                    z += [seqaddr(x[i], y[i])]
                return z
            else:
                return "Matrices are not the same shape"
        else:
            return "This ain't a matrix mate"
    else:
        return "This ain't a matrix mate"


"""
def multMatrix(x, y):
    if isMatrix(x):
        if isMatrix(y):
            z = []
            for i in range(mylength(x)):
                z += [seqmultr(x[i], y[i])]
            return z
        else:
            return "This ain't a matrix mate"
    else:
        return "This ain't a matrix mate"
"""

print("MATRIX ARITHMETIC TESTS")
print("isMatrix TESTS")
print("Expected False")
print(isMatrix([[1, 2, 3], [1, 3, 3], [1, 2, 3, 4], [1, 2, 3]]))
print("Expected True")
print(isMatrix([[1, 2, 3], [1, 3, 3]]))
print("Expected False")
print(isMatrix([[1, 2, 3], [1, 3, 3], [1, 2, 3, 4], [1, 2, 3], [1, 2, 3, 4, 5]]))
print("matrixShape TESTS")
print("Expected (2,3)")
print(matrixShape([[1, 2, 3], [1, 3, 3]]))
print("Expected (2,10)")
print(matrixShape([[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [4, 3, 2, 1, 0, 9, 8, 7, 6, 5]]))
print("Expected This ain't a matrix mate")
print(matrixShape([[1, 2, 3], [1, 3, 3], [1, 2, 3, 4], [1, 2, 3]]))
print("Expected (4,4)")
print(matrixShape([[1, 2, 3, 4], [1, 3, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]))
print("addMatrix TESTS")
print("Expected [[2,4,6],[2,6,6],[2,6,8]]")
print(addMatrix([[1, 2, 3], [1, 3, 3], [1, 3, 4]], [[1, 2, 3], [1, 3, 3], [1, 3, 4]]))
print("Expected [[2,4,6],[2,6,8]]")
print(addMatrix([[1, 2, 3], [1, 3, 4]], [[1, 2, 3], [1, 3, 4]]))
print("Expected [[2,4,6]]")
print(addMatrix([[1, 2, 3]], [[1, 2, 3]]))
print("Expected Matrices are not the same")
print(addMatrix([[1, 2]], [[1, 2, 3]]))

"""
print(multMatrix([[1, 2, 3], [1, 3, 3], [1, 3, 4]], [[1, 2, 3], [1, 3, 3], [1, 3, 4]]))
print(multMatrix([[1, 2, 3], [1, 3, 3], [1, 3, 4]], [[1, 2, 3], [1, 3, 3], [1, 3]]))
print(multMatrix([[1, 2, 3], [1, 3, 3], [1, 3]], [[1, 2, 3], [1, 3, 3], [1, 3, 4]]))
"""
