# *
# **
# ***
# ****
# *****

row = int(input())
for i in range(row):
    for j in range(i+1):
        print("*",end="")
        if j > i:
            break
    print("")
        
