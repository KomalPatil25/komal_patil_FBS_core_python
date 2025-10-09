def find_missing_number(s1, s2):

    missing_ele_set2 = set()
    for i in s1:
        if(i not in s2):
            missing_ele_set2.add(i)

    missing_ele_set1 = set()
    for i in s2:
        if(i not in s1):
            missing_ele_set1.add(i)

    return missing_ele_set1, missing_ele_set2

s1 = {1, 2, 3, 4, 5, 6}
s2 = {2, 3, 6, 7, 8}

missing_ele_set1, missing_ele_set2 = find_missing_number(s1, s2)

print("Number missing in set2 as compared to set1:", missing_ele_set2)
print("Number missing in set1 as compared to set2:", missing_ele_set1)