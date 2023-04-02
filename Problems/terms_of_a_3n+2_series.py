# Write a program to print first x terms of the series 3N + 2 which are not multiples of 4.

x = int(input())
n = 1
while True:
    current = (3 * n) + 2
    if current % 4 != 0:
        print(current, end=" ")
        x -=1
    n +=1
    if x<1:
        break
