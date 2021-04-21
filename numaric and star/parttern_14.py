"""
1   2   3   4   5
16  17  18  19  6
15  24  25  20  7
14  23  22  21  8
13  12  11  10  9


"""

number = int(input("Enter any number ......."))

n_list = [[0 for col in range(number)] for row in range(number)]
low = 0
high = number-1
n = 1
box_number  = (number+1)//2

for box in range(box_number):
    print("STEP : ",box)
    for col in range(low, high+1):
        n_list[low][col] = n
        n += 1

    for row in range(low+1, high+1):
        n_list[row][high] = n
        n += 1

    for col in range(high-1, low-1, -1):
        n_list[high][col] = n
        n += 1
    
    for row in range(high-1, low, -1):
        n_list[row][low] = n
        n += 1
    
    low += 1
    high -= 1


    



for row in range(number):
    for col in range(number):
        print(n_list[row][col],end='\t')
    print()
