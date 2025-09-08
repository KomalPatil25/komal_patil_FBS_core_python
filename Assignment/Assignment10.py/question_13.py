li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
new_li = []

for ele in li:
    if(ele % 2 != 0):
        new_li.append(ele)
print(f'Original list: {li}.')
print(f'After removing even number: {new_li}')