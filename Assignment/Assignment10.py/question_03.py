li = [10, 20, 40, 30, 50, 60]
max = li[0]
for i in range(1, len(li)):
    if(li[i] > max):
        smax = max
        max = li[i]
    elif(li[i] < max):
        smax = li[i]

print(f'Second Largest element is: {smax}')
print(max)