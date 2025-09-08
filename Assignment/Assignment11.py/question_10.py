list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

for item in list:
    if(item % 2 != 0):
        result.append(item)

print("Before removing even no: ", list)
print("After removing even no: ", result)