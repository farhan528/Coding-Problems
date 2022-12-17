def reverseString(str):
    print(str[len(str)-1],end="")
    if len(str)==1:
        return
    reverseString(str[:-1])


str = "abc"
reverseString(str)