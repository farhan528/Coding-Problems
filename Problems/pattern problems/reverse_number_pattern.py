# 1
# 21
# 321
# 4321

n = int(input())

for i in range(1, n+1):
    for j in range(i):
        print(i, end="")
        i -= 1
    print()
