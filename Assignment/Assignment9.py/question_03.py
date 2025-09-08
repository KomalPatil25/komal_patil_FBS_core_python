def revNum(num, rev = 0):
    if(num == 0):
        return rev
    else:
        rev = rev * 10 + (num % 10)
        return revNum(num // 10, rev)
    
num = int(input("Enter the number: "))
res = revNum(num)
print(f'Reverse number: {res}')
    
