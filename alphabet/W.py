'''
*     *
*     *
*     *
*  *  *
* * * *
**   **
*     *

'''
size = 7
row_no = size
if size%2:
    col_no = size
else:
    col_no = size+1
star = "*"

col_mid = (col_no//2)
row_mid = (row_no//2)

for row in range(row_no):
    for col in range(col_no):
        if col == 0 or col == (col_no-1) or ((row_mid<row<row_no-1) and (col+row == (col_no-1))) or (row==col and (row_mid-1<row<row_no-1)):
            print(star,end="")
        else:
            print(end=" ")
    print()
