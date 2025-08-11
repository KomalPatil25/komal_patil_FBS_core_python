side1 = int(input("Enter the side 1: "))
side2 = int(input("Enter the side 2: "))
side3 = int(input("Enter the side 3: "))

# triangle_side = side1 * side2 * side3

if((side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1)):
    print("side of triangle is valid")
else:
    print("side of triangle is invalid")