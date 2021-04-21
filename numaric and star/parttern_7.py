'''
* * * * *
  *     *
    *   *
      * *
        *
'''
line = int(input("Enter the number of line "))
for row in range(0,line):
    for col in range(0,line):
        if (row == col) or (col == (line-1)) or (row == 0):
            print('*',end=' ')
        else:
            print(end="  ")
    print()