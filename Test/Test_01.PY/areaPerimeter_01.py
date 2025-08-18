length = int(input("enter the length of rectangle: "))
breadth = int(input("enter the breadth of rectangle: "))
radius = int(input("enter the radius of the semicircle: "))

 
area_rectangle = length * breadth
area_semicircle = (1/2) * 3.14 * radius * radius
total_area = area_rectangle + area_semicircle

perimeter = (2 * length) + breadth +(3.14 * radius)

print(f"The area is {total_area} and perimeter is {perimeter}.")

