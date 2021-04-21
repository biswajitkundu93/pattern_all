'''
 
***** 
*     
*     
*     
*  ***
*   * 
***** 

'''

size = 7
row_no = size
col_no = (size - 1)
star = "*"

fix = row_no - (row_no//2)
fix_col = (size//2)+1

for row in range(row_no):
    for col in range(col_no):
        if (col == 0) or (((row == 0) or (row == (row_no - 1))) and (col<(col_no-1))) or (((col_no-fix_col)<col<col_no) and (row == fix)) or ((col == (col_no-2)) and (row > fix)):
            print(star,end="")
        else:
            print(end=" ")
    print()
