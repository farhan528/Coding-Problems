# A
# BC
# CDE
# DEFG

first = 65
n = int(input())

for i in range(n):
    for j in range(i+1):
        print(chr(first+i), end="")
        i +=1
    print()
