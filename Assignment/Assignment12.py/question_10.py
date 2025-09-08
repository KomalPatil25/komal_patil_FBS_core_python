# str1 = input("Enter the string1: ")
# str2 = input("Enter the string2: ")

# count1 = 0
# for ele in str1:
#     count1 += 1

# count2 = 0
# for ele in str2:
#     count2 += 1

# if(count1 > count2):
#     print("String1 is larger.")
# elif(count1 < count2):
#     print("String2 is larger.")
# else:
#     print("Both are same.")

def length(s):
    count = 0
    for ele in s:
        count += 1
    return count

def stringLength(str1, str2):
    len1 = length(str1)
    len2 = length(str2)

    if(len1 > len2):
        return str1
    elif(len1 < len2):
        return str2
    else:
        return 'Both are same'

str1 = input("Enter the string: ")
str2 = input("Enter the string: ")
res = stringLength(str1, str2)
print(res)