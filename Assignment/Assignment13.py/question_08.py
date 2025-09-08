str = 'FirstBit is a educational institude. FirstBit is a educational institude.'
word = str.split()

count = {}
for i in word:
    count[i] = count.get(i, 0) + 1
print(count)