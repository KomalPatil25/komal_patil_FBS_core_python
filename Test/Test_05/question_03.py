# using function
def sort(li):
    for i in range(0, len(li)-1):
        for j in range(0,len(li)-i-1):
                if(li[j][2] > li[j + 1][2]):
                      li[j], li[j + 1] = li[j + 1], li[j]
                      return li

li = [[101, "Seema", 45000], [340, "Rajani", 13000], [210, "Tannu", 14000], [320, "Suresh", 35000]]
print("Before sorting: ", li)
li = sort(li)
print("After sorting: ", li)






