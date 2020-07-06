def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:  # Zero exception if divided by zero
        print("Handled div by zero exception")
        return 0


def main():
    validinput: bool = False
    while not validinput:
        try:
            x = int(input("Enter a number"))
            y = int(input("Enter another number"))
            print("For 'add' type 1")
            print("for 'sub' type 2")
            print("for 'mult' type 3")
            print("for 'div' type 4")
            operation = int(input("Enter the key for the operation"))
            validinput = True
        except ValueError:
            print("Invalid input")
    if operation == 1:
        print(add(x, y))
    elif operation == 2:
        print(sub(x, y))
    elif operation == 3:
        print(mult(x, y))
    elif operation == 4:
        print(div(x, y))
    else:
        print("whoopsie poopsie")


main()
