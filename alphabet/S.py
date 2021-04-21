'''
 ***** 
*      
*      
 ***** 
      *
      *
 ***** 
 '''
size = 7
row_no = size
col_no = (size -1)
star = "*"

row_mid = row_no//2
col_mid = col_no//2

for row in range(row_no):
    for col in range(col_no):
        if ((row == 0 or row == row_mid or row == (row_no-1)) and (0<col<(col_no-1))) or (col == 0 and (0<row<row_mid)) or (col == (col_no-1) and ((row_no-1)>row>row_mid)):
            print(star,end="")
        else:
            print(end=" ")
    print()
