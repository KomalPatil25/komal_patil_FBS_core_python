def remove_odd_index(str):
    result = ' '
    for item in range(len(str)):
        if(item % 2 == 0):
            result += str[item]
    return result

str = 'I am learning python.'
res = remove_odd_index(str)
print("Removing odd index:", res)