List1 = [10, 20, 30, 40, 50]
List2 = [40, 50, 60, 70, 80]

intersection = []

for ele in List1:
    if(ele in List2 and ele not in intersection):
        intersection.append(ele)

print('List1 is: ', List1)
print('List2 is: ', List2)
print('Intersection: ', intersection)