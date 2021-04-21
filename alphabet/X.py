'''

*     *
 *   * 
  * *  
   *   
  * *  
 *   * 
*     *

'''
size = 7
row_no = size
if size%2:
    col_no = size
    
else:
    col_no =  size+1
star = "*"

for row in range(row_no):
    for col in range(col_no):
        if (col == row) or (col+row == (col_no-1)):
            print(star,end="")
        else:
            print(end=" ")
    print()
