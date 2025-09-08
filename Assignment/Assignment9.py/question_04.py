def sum_num(num):
    if(num == 0):
        return 0
    else:
        return num + sum_num(num - 1)
    
num = int(input("Enter the number: "))
res = sum_num(num)
print(res)