def bubbleSort(li):
    for i in range(1, len(li)):
        for j in range(0, len(li) - i):
            if(li[i] > li[j + 1]):
                li[j], li[j + 1] = li[j + 1], [li[j]]
            return li
    else:
        return -1
    
li = [10, 20, 30, 40, 50]
li1 = bubbleSort(li)
second_largest = li1[-2]
print("After sorting: ", li1)
print("Secong largect number: ", second_largest)