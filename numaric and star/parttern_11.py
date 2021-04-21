'''
    *
  *   *
*       *
  *   *
    *
 '''

n = int(input("Enter any even number ........!"))
mid = n//2
for row in range(n+1):
    for col in range(n+1):
        if (col+row == mid) or (col-row  == mid) or (row-col == mid) or (col+row == mid+n):
            print("*",end="")
        else:
            print(end=" ")
    print()
