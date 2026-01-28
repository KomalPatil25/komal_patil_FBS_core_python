li1 = [10, 20, 30, 40, 50, 60]
li2 = [40, 50, 60, 70, 80, 90]

union_li = []

for ele in li1:
    if(ele not in union_li):
        union_li.append(ele)

for ele in li2:
    if(ele not in union_li):
        union_li.append(ele)

print("List 1 is: ", li1)
print("List 2 is: ", li2)
print("Union set is: ",union_li)