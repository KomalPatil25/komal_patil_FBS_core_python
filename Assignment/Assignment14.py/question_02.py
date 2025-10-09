set1 = {100, 200, 300, 400, 500}
set2 = { 500, 400,600, 700, 800, 900, 1000}

set1.difference_update(set2)
print("Set1 after removing intersection: ", set1)