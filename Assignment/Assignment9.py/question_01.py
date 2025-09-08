def fact(num):
    if(num == 0):
        return 1
    else:
        return num * fact(num - 1)

def sumSeries(num):
    if(num == 1):
        return fact(1)
    else:
        return fact(num) + sumSeries(num - 1)
    
num = int(input("Enter the number: "))
result = sumSeries(num)
print(result)