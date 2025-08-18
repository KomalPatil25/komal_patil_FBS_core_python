def areaCircle(r):

    area = 3.14 * r * r
    return area

r = int(input("Enter radius to calculate area of circle: "))
result = areaCircle(r)
print(f"The area of circle is {result}.")