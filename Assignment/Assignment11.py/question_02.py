li1 = [2, 4, 6, 8, 1, 5]
li2 = [7, 8, 3, 6, 9, 2]
li3 = []

for i in range(len(li1)):
    li3.append(li1[i])
for i in range(len(li2)):
    li3.append(li2[i])

# print(li3)

# sort list using bubble sort
def sortList(li3):
    for i in range(1, len(li3)):
        for j in range(0, len(li3) - 1):
            if(li3[j] > li3[j + 1]):
                li3[j], li3[j + 1] = li3[j + 1], li3[j]
    return li3

res = sortList(li3)
print(res)