str = 'I am learning python at firstBit solution.'

count = 0
for i in str:
    if(i.islower()):
        count+=1

print("Number of lowercase character: ",count)