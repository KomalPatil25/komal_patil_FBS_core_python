def is_anagram(str1, str2):
    if(len(str1) != len(str2)):
        return False
    
    count = {}
    for ch in str1:
        if(ch in count):
            count[ch] += 1
        else:
            count[ch] = 1

    for ch in str2:
        if(ch not in count):
            return False
        
        count[ch] -= 1
        if(count[ch] < 0):
            return False
        
    for val in count.values():
        if(val != 0):
            return False
        else:
            return True
        
str1 = input("Enter the string1: ")
str2 = input("Enter the string2: ")
res = is_anagram(str1, str2)
print(res)

    

  
