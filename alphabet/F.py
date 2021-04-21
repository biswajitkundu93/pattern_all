'''
 
******
*     
*     
******
*     
*     
*

'''

size = 7
row_no = size
col_no = (size - 1)
star = "*"

for row in range(row_no):
    for col in range(col_no):
        if (col == 0) or ((row == 0)  and (col<col_no)) or (row == (row_no//2)):
            print(star,end="")
        else:
            print(end=" ")
    print()
