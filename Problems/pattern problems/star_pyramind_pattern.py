#    *
#   ***
#  *****
# *******



n = int(input())

for i in range(n):
    count_space = 0
    for spaces in range(n-i-1):
        print(" ", end="")
        count_space +=1
    for num in range(count_space, n+i):
        print("*", end="")
    print()        
