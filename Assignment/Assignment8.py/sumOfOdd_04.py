def sumOdd(num):

    total = 0
    for i in range(1, num + 1):
        if(i % 2 != 0):
            total += i
            
    return total

num = int(input("Enter the number: "))
res = sumOdd(num)
print(f"The sum of odd numbers from 1 to {num} is: {res}")
