def pattern(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1 - i):
            if(i == 1):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        for j in range(1, i + 1):
            if(i == num or j == 1):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
num = int(input("Enter the number: "))
pattern(num)