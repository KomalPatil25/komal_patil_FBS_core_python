# str = 'I am learning python at firstBit solution.'

# result = ' '
# for ele in str:
#     if(ele == ' '):
#         result += '-'
#     else:
#         result += ele

# print(result)    

def space_hyphen(str):
    result = ' '
    for ele in str:
        if(ele == ' '):
            result += '-'
        else:
            result += ele
    return result

str = 'I am learning python at firstBit solution.'
res = space_hyphen(str)
print("Original String: ", str)
print("Midified String: ", res)