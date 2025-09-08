li = [10, 40, 20, 30, 50]
max = li[0]
min = li[0]
for i in range(1, len(li)):
    if(li[i] > max):
        max = li[i]
        
    if(li[i] < min):
        min = li[i]

print(f'Maximum number is: {max}')
print(f'Mimimum number is: {min}')
