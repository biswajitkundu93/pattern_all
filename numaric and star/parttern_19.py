'''
1
2 9
3 8 10
4 7 11 14
5 6 12 13 15

'''
num = int(input("Enter the number of rows: "))

for row in range(num):
    for col in range(row+1):
        last_col_val = 0
        for k in range(col):
            last_col_val = last_col_val + num - k
        if col%2 == 0:
            print(last_col_val + row - col + 1 ,end=" ")
        else: 
            print(last_col_val + num - row , end=" ")
    print()