'''
*             *
 *           * 
  *         *  
   *       *   
    *     *    
     *   *     
      * *      
       * 
       
'''

size = 7
row_no = size
col_no = size
star = "*"

col_mid = (col_no//2)

for row in range(row_no+1):
    for col in range(col_no+col_no+1):
        if col == row or row == (col_no+col_no-col):
            print(star,end="")
        else:
            print(end=" ")
    print()
