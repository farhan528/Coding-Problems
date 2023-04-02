# Write a program that asks the user for a number N and a choice C. And then give them the possibility
# to choose between computing the sum and computing the product of all integersin the range 1 to N (both inclusive).

n = int(input())
c = int(input())
add, prod = 0, 1
if c == 1:
    for i in range(1, n+1):
        add+=i
    print(add)
elif c ==2:
    for i in range(1, n+1):
        prod *= i
    print(prod)

else:
    print(-1)
