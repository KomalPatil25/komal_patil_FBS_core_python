li = [70, 50, 60, 30, 33, 20]
rev = []

for i in range(len(li)-1, -1, -1):
    rev.append(li[i])
print(f'Reverse List: ',rev)