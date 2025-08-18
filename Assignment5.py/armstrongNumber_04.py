num = int(input("Enter the number: "))

temp = num
num_digit = 0
while(temp > 0):
    temp = temp // 10
    num_digit += 1

temp = num
sum_power = 0
while(temp > 0):
    digit = temp % 10
    sum_power += digit ** num_digit
    temp //= 10

if(num == sum_power):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")