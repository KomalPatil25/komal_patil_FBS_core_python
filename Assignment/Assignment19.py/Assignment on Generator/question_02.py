def palindrome_numbers():
    num = 0
    while True:
        if str(num) == str(num)[::-1]:
            yield num
            num += 1

gen = palindrome_numbers()
for _ in range(20):
    print(next(gen))