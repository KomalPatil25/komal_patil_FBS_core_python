def prime(num):
    if(num < 2):
        return False
    else:
        for i in range(2, num):
            if(num % i == 0):
                return False
            else:
                return True
    
num = int(input("Enter the number: "))
res = prime(num)
print(res)