'''
  * * * *
*    *    *
*         *
  *     *
    * *
     *
'''
# n = int(input("Enter any even number ........!"))
# mid = n//2
n=6
for row in range(n):
    for col in range(n+1):
        if ((row == 0) and (col%3 != 0)) or ((row == 1) and (col%3 == 0)) or (row-col == 2) or (col+row == 8):
            print("*",end="")
        else:
            print(end=" ")
    print()
