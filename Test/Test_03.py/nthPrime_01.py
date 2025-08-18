num = int(input("enter the number to check prime or not: "))

count = 0
n1 = 2
while(count < num):
    prime = True
    for i in range(2, n1 // 2 + 1):
        if(n1 % i == 0):
            prime = False
            break
    else:
        print(n1, end=" ")
        count += 1

    n1 += 1