def count_digit(num):
    if(num == 0):
        return 0
    else: 
        return 1 + count_digit(num // 10)

def armstrong_sum(num, power): 
    if(num == 0):
        return 0
    else:
        digit = num % 10
        return (digit ** power) + armstrong_sum(num // 10, power)

def is_armstrong(num):
    n = count_digit(num)
    if(num == armstrong_sum(num, n)) :   
        return True
    else:
        return False
    
num = int(input("Enter the number: "))
res = is_armstrong(num)
if(res):
    print(f'{num} is armstrong number.')
else:
    print(f'{num} is not armstrong number.')