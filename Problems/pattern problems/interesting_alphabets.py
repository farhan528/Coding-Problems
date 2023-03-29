# E
# DE
# CDE
# BCDE
# ABCDE


first = 65
n = int(input())

for i in range(n):
    temp = (n - i) - 1
    for j in range(i+1):
        print(chr(first+temp), end="")
        temp +=1
    print()
