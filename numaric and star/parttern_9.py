'''
1 2 3 4 
1 2 3 
1 2 
1 

4 4 4 4
3 3 3
2 2 
1
'''

line = int(input("Enter the number of line "))
for row in range(line,0, -1):
    for col in range(1,row+1):
        print(col,end=" ")
    print()

print('\n')
for row in range(line,0, -1):
    for col in range(1,row+1):
        print(row,end=" ")
    print()
