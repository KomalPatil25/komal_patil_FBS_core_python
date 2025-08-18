year = int(input("Enter the year: "))

if(year % 4 == 0 ):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(f"{year} year is leap year.")
        else:
            print(f"{year} year is not leap year.")
    else:
        print(f"{year} year is leap year.")
else:
    print(f"{year} Year is not leap year.")

