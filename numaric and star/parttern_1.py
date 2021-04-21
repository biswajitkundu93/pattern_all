'''
*
**
***
****
'''

line = int(input("Enter the number of line "))
'''
for i in range(line):
    for j in range(i):
        print("*",end=" ")
    print()
'''

for i in range(line):
    print("*"*(i+1),end=" ")
    print()
