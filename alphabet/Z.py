'''
*******
     * 
    *  
   *   
  *    
 *     
*******

'''

size = 7
row_no = size
col_no = (size - 1)
star = "*"

for row in range(row_no):
    for col in range(col_no+1):
        if (row == 0) or (row == (row_no-1)) or (row+col == (col_no)):
            print(star,end="")
        elif row==0 and col==col_no:
            print(star,end="")
        else:
            print(end=" ")
    print()
