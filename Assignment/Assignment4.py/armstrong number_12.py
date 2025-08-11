# n1 = int(input("Enter the number: "))
# n2 = int(input("Enter the number: "))

# for num in range(n1, n2+1):
#     digits = str(num)
#     power = len(digits)
#     sum_power = sum(int(d)**power for d in digits)

#     if(sum_power == num):
#         print(num, end=" ")

n1 = int(input("Enter the number: "))

for num in range(1, n1+1):
    digits = str(num)
    power = len(digits)
    sum_power = sum(int(d)**power for d in digits)

    if(sum_power == num):
        print(num, end=" ")

    