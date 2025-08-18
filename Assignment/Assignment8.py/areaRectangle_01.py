def areaRec(length, breadth):

    area = length * breadth
    return area

length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
res = areaRec(length, breadth)
print(f"The area of rectangle is {res}.")