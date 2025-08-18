height = int(input("enter the height: "))
width = int(input("enter the width: "))
cost_sq_meter = int(input("enter cost of painting per square meter: "))

area_one_wall = height * width
total_area = area_one_wall * 4
total_cost = total_area *cost_sq_meter

print(f'Total area to be painted is {total_area}.\nTotal cost of painting {total_cost}')