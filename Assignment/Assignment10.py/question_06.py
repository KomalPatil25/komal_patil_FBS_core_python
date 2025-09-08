li = [89, 45, 36, 89, 10, 28, 45]
new_li = []

for i in range(len(li)):
    if(li[i] not in new_li):
        new_li.append(li[i])
        
print(f'Original list: {li}.')
print(f'After removing duplicate the list is: {new_li}.')