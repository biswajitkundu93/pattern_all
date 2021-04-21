'''
   1
  212
 32123
4321234
'''

num = int(input("Enter a number "))

'''
temp = "".join([str(i) for i in range(1,Number+1)])
string = temp[::-1]+temp[1:]

low = 0 
high = len(string)-1

for i in range(Number-1, -1, -1):
    print(" "*i,string[low+i:high-i+1])
'''
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(i, 0, -1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()