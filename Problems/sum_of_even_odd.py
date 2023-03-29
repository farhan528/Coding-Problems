# Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.
# Digits mean numbers, not the places! That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.


def sumEvenOdd(num):
    rem, rev = 0, 0
    temp = num
    sum_even,sum_odd = 0,0
    while(temp!=0):
        rem = temp % 10
        if rem % 2 == 0:
            sum_even = sum_even + rem
        else:
            sum_odd = sum_odd + rem
        temp = temp // 10
    print(sum_even, sum_odd)
		
n = int(input())
sumEvenOdd(n)
