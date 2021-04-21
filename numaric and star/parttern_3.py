'''
   *
  * *
 * * *
* * * *

'''
line = int(input("Enter the number of line "))
'''
for i in range(line):
    for j in range(line-i-1):
        print(end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
'''
for i in range(line):
    print(' '*(line-i-1)+'* '*(i+1))
