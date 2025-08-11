angle1 = int(input("Enter the angle 1: "))
angle2 = int(input("Enter the angle 2: "))
angle3 = int(input("Enter the angle 3: "))

triangle = angle1 + angle2 + angle3

if(triangle == 180):
    print(f"{triangle} Triangle is valid")

else:
    print(f"{triangle} Triangle is ivalid")

