def string_space(str):
    result = ' '
    for ele in str:
        if(ele == ' '):
            result += '-'
        else:
            result += ele
    return result

str = "I am learning python language."
res = string_space(str)
print("Original string: ", str)
print("After modified: ", res)