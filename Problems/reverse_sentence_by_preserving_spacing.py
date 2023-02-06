# i/p: My name if farhan
# o/p: na hraF si emanyM

def getReverse(name):
    n = len(name)
    result = [0]*n
    for i in range(n):
        if name[i] == ' ':
            result[i] = ' '
    j = n-1
    for i in range(n):
        if name[i] != ' ':
            if result[j] == ' ':
                j-=1
            result[j] = name[i]
            j-=1
    return ''.join(result)


name = "My name is Farhan"
print(getReverse(name))
