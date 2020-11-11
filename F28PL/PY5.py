# ######################################################################################################################
# Question 5
# Encoding

"""Take in any value convert to a string and remove brackets if its in brackets. Then we use repr to place item in ''
for the output """


def encdat(x):
    conversion = str(x)
    if type(x) == type(1+1j):
        conversion = conversion.strip(")")
        conversion = conversion.strip("(")
    return repr(conversion)


print("QUESTION 5 TESTS")
print("Expected 'EUAN, EUAN' ")
print(encdat(('EUAN', 'EUAN')))
print("Expected '-5' ")
print(encdat(-5))
print("Expected '0.5' ")
print(encdat(0.5))
print("Expected '5+5j' ")
print(encdat(5+5j))
print("Expected '5' ")
print(encdat('5'))
print("Expected false ")
print(type(-5) == encdat(-5))
