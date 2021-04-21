'''
        *
       *A*
      *A*A*
     *A*A*A*
    *A*A*A*A*
   *A*A*A*A*A*
  *A*A*A*A*A*A*
 *A*A*A*A*A*A*A*
*A*A*A*A*A*A*A*A*
'''

n = int(input("Enter a number ....."))
colume = 2*n -1
mid = colume//2

for row in range(n):
    print(" "*(n-row-1),end="")
    count = 0
    for col in range(row+1):
        print('*',end='')
        if count < row:
            print('A',end='')
            count += 1
        
    print()
