n = 10
num = 1
for row in range(1, n + 1):
    row_num = list(range(num, num + n))
    num += n

    if(row % 2 == 0):
        row_num.reverse()

    for x in row_num: 
        print(x, end=" ")

    print()