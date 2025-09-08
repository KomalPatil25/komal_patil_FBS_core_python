def count(str):
    count = 0
    for item in str:
        count += 1
    return count

def largest_string(str1, str2):
    len1 = count(str1)
    len2 = count(str2)

    if(len1 > len2):
        return 'String1 is greater.'
    elif(len1 < len2):
        return 'String2 is greater.'
    else:
        return 'Both are same.'
    
str1 = input("Enter the string1: ")
str2 = input("Enter the string1: ")
res = largest_string(str1, str2)
print(res)