str = 'I am learning python at firstBit solution 181225.'

result = 0
for item in str:
    if(item.isalnum()):
        result += 1

print("Number of digit and letters in string: ",result)