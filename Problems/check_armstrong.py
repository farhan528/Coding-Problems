import math
num = int(input("Enter the number to check for Armstrong: "))
sum = 0
list_num = [int(d) for d in str(num)]
for i in range(len(list_num)):
    sum = sum + (list_num[i]**3)
if(num == sum):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
