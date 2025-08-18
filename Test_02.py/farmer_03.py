# fancing = int(input("Enter the fancing: "))

# r = 20/100
# l = 50/100
# b = 40/100

# barbed_wire = 5
# cost_fancing = r * l * b

# print(f"the barbed wired 5 times is {barbed_wire}. Total cost of fencing is {cost_fancing}")

r = 20
l = 50
b = 40
barbed_wire = 5
cost_per_m = 35

rec_edge = 2 * l + b

semicircle_arc = 3.14 * r

perimeter = rec_edge + semicircle_arc

total_wire = barbed_wire * perimeter

total_cost = total_wire * cost_per_m

print(f'Perimeter of field (one round): {perimeter}m.')
print(f'Total wire needed: {total_wire}m.')
print(f'Total fencing cost: {total_cost}.')


