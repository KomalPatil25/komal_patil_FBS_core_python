def len_count(str):
    count = 0
    for item in str:
        count += 1
    return count
    
str= 'Komal Patil'
res = len_count(str)
print("Ength of string is: ", res)