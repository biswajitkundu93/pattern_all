'''

*    *
*    *
*    *
******
*    *
*    *
*    *

'''
size = 7
row_no = size
col_no = (size - 1)
star = "*"

for row in range(row_no):
    for col in range(col_no):
        if (col == 0) or (col == (col_no-1)) or (row == (row_no//2)) :
            print(star,end="")
        else:
            print(end=" ")
    print()
