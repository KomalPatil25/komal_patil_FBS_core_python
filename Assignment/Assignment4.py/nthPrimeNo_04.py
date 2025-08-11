n = int(input("Enter the number: "))

count = 0
num = 2
while(count < n):
    for i in range(2, num // 2 + 1):
        if(num % i == 0):
            # print("Not prime")
            print(num)
            break
    else:
        print(num, "Prime number")
        count += 1

    num += 1