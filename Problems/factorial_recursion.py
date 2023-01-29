def getFact(num):
    if num <= 1:
        return 1
    else:
        return num * getFact(num-1)

num = int(input("Enter the number for Factorial: "))
print(getFact(num))
