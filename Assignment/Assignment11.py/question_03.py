def sort_second(li):
    for i in range(len(li)):
        for j in range(len(li) - i - 1):
            if(li[j][1] > li[j+1][1]):
                li[j], li[j+1] = li[j+1], li[j]
    return li

li = [[1, 5], [3, 2], [4, 8], [2, 1], [9, 4]]
print("Original List: ", li)
sorted_list = sort_second(li)
print("Sorted by second element: ", sorted_list)