def leapYear(year):
    if((year % 4 == 0) or (year % 100 == 0) or (year % 400 == 0)):
        return True
    else:
        return False

year = int(input("enter the year to check leap year or not: "))
if(leapYear(year)):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")