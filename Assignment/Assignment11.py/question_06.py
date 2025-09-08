list1 = [11, 12, 13, 14, 15]
list2 = [14, 15, 16, 17, 18]

union_list = []

for ele in list1:
    if(ele not in union_list):
        union_list.append(ele)

for ele in list2:
    if(ele not in union_list):
        union_list.append(ele)

print("List1 is: ", list1)
print("List2 is: ", list2)
print("Union List: ", union_list)