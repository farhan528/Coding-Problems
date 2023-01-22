num = int(input("Enter the number to reverse: "))
temp = num
remainder = 0
reverse = 0
while(num!=0):
    remainder = num % 10
    reverse = reverse * 10 + remainder
    num = num // 10
print("Reverse is:", reverse)
if(temp == reverse):
    print("Number is Plaindrome")
else:
    print("Number is not Palindrome")
