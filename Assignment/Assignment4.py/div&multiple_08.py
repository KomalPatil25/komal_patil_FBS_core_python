num1 = int(input("enter the 1st number: "))

for i in range(1, num1+1):
    if(i % 7 == 0 and i % 5 == 0):
        print(i, end=" ")