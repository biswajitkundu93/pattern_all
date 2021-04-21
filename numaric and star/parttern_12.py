'''
   *
  * *
 *   *
*******

   *
  * *
 *   *
* * * *
'''

n = int(input("Enter any  number ........!"))
colume = 2*n - 1 
mid = colume//2
for row in range(n):
    for col in range(colume):
        if (col+row == mid)  or (col-row == mid) or (row == n-1):
            print("*",end="")
        else:
            print(end=" ")
    print()

print()
for row in range(n):
    for col in range(colume):
        if (col+row == mid)  or (col-row == mid) or (row == n-1 and col%2 == 0):
            print("*",end="")
        else:
            print(end=" ")
    print()