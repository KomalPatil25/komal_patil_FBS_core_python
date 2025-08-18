area = int(input("Enter the area of wall: "))
interior = int(input("Enter the cost of interior: "))
exterior = int(input("Enter the cost of exterior: "))

total_wall = 6
interior_wall = 6
exterior_wall = 2

total_interior_area = area * interior_wall
total_exterior_area = area * exterior_wall

interior_paint_cost = total_interior_area * interior
exterior_paint_cost = total_exterior_area * exterior

total_cost = interior_paint_cost + exterior_paint_cost

print(f'''The cost of painting interior is {interior}. & exterier is {exterior}.\ninterior paint cost {interior_paint_cost}.\nexterior paint cost {exterior_paint_cost}.\nTotal painting cost{total_cost}''')