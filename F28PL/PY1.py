# #####################################################################################################################
# Euan Gordon
# F28PL
# ejg9@hw.ac.uk
# Question 1
# Complex number Arithmetic


"""CADD takes in two tuples, gets the indexes and adds the accordingly and assigns them x1 and y1 and returns a tuple
of x1 and y1 """


def cadd(x, y):
    x1 = x[0] + y[0]
    y1 = x[1] + y[1]
    return x1, y1


"""CMULT takes in two tuples, gets the indexes and multiplies accordingly and out puts the numbers x1 and y1 as a 
tuple """


def cmult(x, y):
    x1 = (x[0] * y[0]) - (x[1] * y[1])
    y1 = (x[0] * y[1]) + (x[1] * y[0])
    return x1, y1


"""toComplex takes in one tuple and assigns a real number and adds it to an imaginary number which is just multiplied 
by 1j """


def tocomplex(x):
    z = x[0].real + x[1] * 1j
    return z


"""fromComplex takes in a complex number and creates a tuple that will contain the real number and the imaginary 
number by using real and imag to get rid of the j in imaginary number"""


def fromcomplex(z):
    return z.real, z.imag


print("COMPLEX NUMBER TESTS")
print("Expected (9,8)")
print(cadd((4, 5), (5, 3)))
print("Expected (1,0)")
print(cadd((1, 0), (0, 1)))
print("Expected (-35, 13)")
print(cmult((-4, 5), (5, 3)))
print("Expected (9+8j)")
print(tocomplex(cadd((4, 5), (5, 3))))
print("Expected (-745+100j)")
print(tocomplex(cmult((1, 22), (3, 34))))
print("Expected (9+8j)")
print(tocomplex((9, 8)))
print("Expected (9,8)")
print(fromcomplex(9 + 8j))
print("Expected (-111,-22)")
print(fromcomplex(-111 - 22j))
