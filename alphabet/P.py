
size = 7
row_no = size
col_no = (size - 1)
star = "*"

mid_row = row_no//2

for row in range(row_no):
    for col in range(col_no):
        if (col == 0 and row>0) or ((row == 0 or row == mid_row) and (0<col<(col_no-1))) or ((col == (col_no-1)) and (0<row<mid_row)):
            print(star,end="")
        else:
            print(end=" ")
    print()
