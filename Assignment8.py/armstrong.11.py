def armstrong(num):
    temp = num
    count = 0
    while(temp > 0):
        count += 1
        temp //= 10
    
    temp = num
    total = 0
    while(temp > 0):
        digit = temp % 10
        total += digit ** count
        temp //= 10

    if(total == num):
        return True
    else:
        return False

num = int(input("Enter the number to check armstrong or not: "))
if(armstrong(num)):
    print(f"{num} is a Armstrong number.")
else:
    print(f"{num} is not a Armstrong number.")