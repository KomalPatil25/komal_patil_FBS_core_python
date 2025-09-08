li = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

square = []
cube = []

for i in li:
    if(i % 2 == 0):
        square.append(i)
    else:
        cube.append(i)

print(li)
print(square)
print(cube)