num = [2, 4, 5, 6, 8, 9, 3, 6, 7]

freq = {}

for i in num:
    if(i in freq):
        freq[i] += 1
    else:
        freq[i] = 1

print("Frequency dictionary: ", freq)