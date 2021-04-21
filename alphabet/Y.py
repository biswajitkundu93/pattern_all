'''
*     *
 *   * 
  * *  
   *   
   *   
   *   
   * 
'''
size = 7
col_no = row_no = size
star = "*"

col_mid = (col_no//2)
row_mid = (row_no//2)


for row in range(row_no):
    for col in range(col_no):
        if ((col==col_mid) and (row>row_mid-1)) or ((row == col) and (col<col_mid)) or ((col+row == col_no-1) and (col>col_mid)):
            print(star,end="")
        else:
            print(end=" ")
    print()
