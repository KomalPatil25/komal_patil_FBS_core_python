coins = int(input("enter the missing coin: "))
list = [2, 4, 7, 4, 8, 9, 2, 7, 4, 9, 4,]

count = {}
for i in list:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for num in count:
    if(count[num] % 2 != 0):
        print("Missing coin number: ", num)
        break