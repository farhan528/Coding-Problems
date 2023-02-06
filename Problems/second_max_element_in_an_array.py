my_list = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
mx, second, current = -2147483648, -2147483648, -2147483648
for i in range(len(my_list)):
    current = my_list[i]
    if current > mx:
        second = mx
        mx = current
    elif current > second and current!=mx:
        second = current
        
print("Max is: ", mx, "and second max is: ", second)
