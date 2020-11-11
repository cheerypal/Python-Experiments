# ######################################################################################################################
# Question 7
# Generators


def mylength(x):
    n = 0
    for i in x:
        n += 1
    return n


"""Created a generator that is identified when yield is placed in the function. I used a while loop so that the list 
would loop infinitely. Yield here will log the current iteration of the list x so when next(f) is called the next 
iteration is printed without starting from the beginning! """


def cycleOfLife():
    x = ["eat", "sleep", "code"]
    i = 0
    while True:
        yield x[i]
        i += 1
        if i >= mylength(x):
            i = 0


"""Set f to the generator so that it can be called with the next method!"""

print("Expected replication of an infinite list!")
f = cycleOfLife()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

