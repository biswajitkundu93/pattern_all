'''
 **** 
*    *
*    *
*    *
*    *
*    *
 **** 
 
'''

size = 7
row_no = size
col_no = (size - 1)
star = "*"

for row in range(row_no):
    for col in range(col_no):
        if ((0 < row < (row_no-1)) and ((col == 0) or (col == (col_no-1)))) or ((0 < col < (col_no-1)) and ((row == 0) or (row == (row_no-1))) )  :
            print(star,end="")
        else:
            print(end=" ")
    print()
