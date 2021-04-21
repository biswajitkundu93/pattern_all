'''
*   * 
*  *  
* *   
**    
* *   
*  *  
*   * 
'''

size = 7
row_no = size
col_no = (size -1)
star = "*"


mid = col_no//2
fix = (row_no//2)+1

for row in range(row_no):
    for col in range(col_no):
        if (col == 0)  or ((row - col == mid-1) and col>0) or ((row + col == mid+1) and row<fix):
            print(star,end="")
        else:
            print(end=" ")
    print()
