digit = int(input("Enter the 3 digit number: "))

if(digit >= 100 and digit <= 999):
    first_digit = digit // 100
    second_digit = (digit // 100) % 10
    third_digit = digit % 10

    if(first_digit * 2 == second_digit and first_digit * 2 == third_digit):
        print("Yes, you have done it.")
    else:
        print("Please try next time.")
else:
    print("That is not a 3 digit number. Please try again.")
