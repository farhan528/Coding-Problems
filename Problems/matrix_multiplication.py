a =[[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
b =[[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
c = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]
for row in range(len(a)):
    b_col = 0
    for curr_col in range(len(a[row])+1):
        sum = 0
        b_row = 0
        for k in range(len(a[row])):
            sum += a[row][k] * b[b_row][b_col]
            b_row += 1
        c[row][curr_col] = sum
        b_col += 1
print(c)
        
