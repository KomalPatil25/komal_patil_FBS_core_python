def find_pairs(li, target):
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if(li[i] + li[j] == target):
                print(li[i], li[j])

li = [2, 4, 3, 7, 1, 5, 9, 6]
target = 10
find_pairs(li, target)
# print(res)