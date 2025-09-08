li = [2, 3, 54, 32, 87, 56, 48, 91, 47, 90, 38, 19]

m = int(input("Enter the number: "))
n = int(input("Enter the number: "))

result = []
for i in li:
    if(i % m == 0 and i % n == 0):
        result.append(i)
print(f'Numbers divisible by {m} and {n} are: {result}')