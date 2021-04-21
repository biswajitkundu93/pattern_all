'''
* * * *
 * * *
  * *
   *
'''
line = int(input("Enter the number of line "))
'''
for i in range(line,0,-1):
    for j in range(line-i):
        print(end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
'''
for i in range(line,0,-1):
    print(' '*(line-i)+'* '*i)