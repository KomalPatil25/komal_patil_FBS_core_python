side1 = int(input("Enter the side 1: "))
side2 = int(input("Enter the side 2: "))
side3 = int(input("Enter the side 3: "))

if((side1 == side2) and (side2 == side3)): # All angle equal
    print("Equilateral triangle")

elif((side1 == side2) or (side2 == side3) or (side1 == side3)): # At list two angle values exact needed
    print("Isosceles triangle")

else:
    print("Scalene triangle")