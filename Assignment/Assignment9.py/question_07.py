def sum_digit(num):
    if(num == 0):
        return 0
    else:
        return (num % 10) + sum_digit(num // 10)
    
num = int(input("Enter the number: "))
result = sum_digit(num)
print(result)