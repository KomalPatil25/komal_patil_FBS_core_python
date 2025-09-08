def reverse(num, rev = 0):
    if(num == 0):
        return rev
    else:
        return reverse(num // 10, rev * 10 + num % 10)
    
num = int(input("enter the number: "))
res = reverse(num)
print(res)