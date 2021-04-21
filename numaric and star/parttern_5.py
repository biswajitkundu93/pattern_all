'''  
     *
    * *
   * * *
    * *
     *
'''
line = int(input("Enter the number of line "))
'''
for i in range(line):
    for j in range(line-i-1):
        print(end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
for i in range(line-1,0,-1):
    for j in range(line-i):
        print(end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
'''
for i in range(line):
    print(' '*(line-i-1)+'* '*(i+1))
for i in range(line-1,0,-1):
    print(' '*(line-i)+'* '*i)