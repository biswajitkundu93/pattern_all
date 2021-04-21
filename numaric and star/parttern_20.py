'''
15
14 10
13 9 6
12 8 5 3
11 7 4 2 1

'''
def k_val (n1):
    if n1==1:
        return 1
    return n1+k_val(n1-1)

num = int(input("Enter the number of rows: "))
#num = 5
k = k_val(num)
for row in range(num):
    val = k-row
    dec = num-1
    for col in range(row+1):
        print(val,end="\t")
        val = val-dec
        dec = dec-1
    print()