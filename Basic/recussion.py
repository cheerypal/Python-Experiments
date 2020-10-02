def mult (m , n):
    if m == 0 or n == 0:
        return 0
    if(m > n):
        return mult(n,m)
    else:
        return m + mult(m , n -1)

print(mult(7, 3))# -> 21
print(mult(1,1))# -> 1
print(mult(-1,1))
print(mult(7,-3))
print(mult(-6,2))