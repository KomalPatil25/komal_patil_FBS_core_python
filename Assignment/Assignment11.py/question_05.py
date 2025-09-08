def sort_length(li):
    for i in range(len(li)):
        for j in range(0, len(li)-1):
            if(len(li[j]) > len(li[j + 1])):
                li[j], li[j + 1] = li[j + 1], li[j]
    return li

li = ['banana', 'mango', 'kiwi', 'apple', 'grapes', 'pineapple']
print("Original list: ", li)
sorted_list = sort_length(li)
print("Sorted lenth of list: ", sorted_list)