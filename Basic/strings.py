# Reverse a String
def reverseString(s):
    newString = ""
    for i in range(len(s))[::-1]:
        newString += s[i]
    
    return newString

print(reverseString("cat"))


#Append an Item to the middle of a String
def appendToCentre(s, character):
    newString = ""
    ls = []
    middle = 0 + (len(s) - 0) // 2
    print(middle)
    for i in range(len(s)):
        if i == middle:
            ls.append(character)    
        ls.append(s[i])

    newString = ''.join(ls)

    return newString
        
    
print(appendToCentre("cats", "l"))

#


