'''

*****
  *  
  *  
  *  
  *  
  *  
*** 

'''

size = 7
row_no = size
col_no = (size - 2)
star = "*"

for row in range(row_no):
    for col in range(col_no):
        if (row == 0) or ((row == (row_no-1)) and (col<col_no//2)) or (col == (col_no//2)) :
            print(star,end="")
        else:
            print(end=" ")
    print()