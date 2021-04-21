'''
1
2 3 
4 5 6
7 8 9 10

'''
line = int(input("Enter the number of line "))

i=0
for row in range(line):
    for col in range(row+1):
        print(i+1,end=" ")
        i+=1
    print()