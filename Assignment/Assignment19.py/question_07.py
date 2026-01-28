num = [x for x in range(1, 1001) if (x % y == 0 for y in range(1, 10))]
print(num)