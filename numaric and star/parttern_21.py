'''
1   5
 2 4 
  3  
 2 4 
1   5

1   1
 2 2 
  3  
 4 4 
5   5

'''

num = int(input("Enter a number ........"))
    
print('\n')
for row in range(1,num+1):
    for col in range(1,num+1):
        if (col == row) or (col+row == (num+1)):
            print(col,end="")
        else:
            print(end=" ")
    print()

print('\n')
for row in range(1,num+1):
    for col in range(1,num+1):
        if (col == row) or (col+row == (num+1)):
            print(row,end="")
        else:
            print(end=" ")
    print()