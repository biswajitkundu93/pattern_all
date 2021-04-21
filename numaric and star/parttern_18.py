'''
1
2 6
3 7 10  
4 8 11 13
5 9 12 14 15

'''

num = int(input("Enter the number of rows: "))

for row in range(num):
    val = row+1
    dec = num-1
    for col in range(row+1):
        print(val,end="\t")
        val = val+dec
        dec = dec-1
    print()