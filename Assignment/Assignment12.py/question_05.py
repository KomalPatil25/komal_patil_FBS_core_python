# str = 'Hey, Hellow my name is komal patil.'
# count = 0
# for ele in str:
#     if(ele in 'aeiouAEIOU'):
#         count += 1

# print(count)

# USING FUNCTION
def count_vowel(str):
    count = 0
    for ele in str:
        if(ele in 'aeiouAEIOU'):
            count += 1
    return count

str = 'I am learning python proramming language.'
result = count_vowel(str)
print("Number of vowels in string is: ", result)